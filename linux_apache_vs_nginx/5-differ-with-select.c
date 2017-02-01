// Допустим, в процессе нужно обрабатывать максимум 30 соединений. Мы создаем массив из нулей. Как только к нам придет новое соединение, мы его обрабатываем, а адрес сокета записываем в этот массив. Перебирая весь массив и все наши сокеты, мы можем последовательно считывать с них информацию. Но как нам узнать о новом соединении без использования вызова accept? В linux для этого есть как минимум 3 функции: select, poll и epoll. А в freebsd для этого есть аналог функции epoll под названием kqueue (kernel queue). Что делают эти команды? select – самая старая функция, которая до сих пор используется для того, чтобы отдавать всё процессорное время ядру, запрашивая его только при определенных условиях (по аналогии с accept). Разница в том, что ядро вернет нам cpu, когда на указанных нами сокетах начнется любая активность. Так как при запуске программы открыт только один сокет, то и в select мы указываем один. Если мы подключимся телнетом к нашему демону, то в select мы должны указывать уже два сокета: мастер сокет на порт 2222 и тот, который к нам подключился.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/time.h>

#define PORT 2222

int main(int argc , char *argv[])
{
    int opt = 1;
    int master_socket , addrlen , new_socket , client_socket[30] , max_clients = 30 , activity, i , valread , sd;
    int max_sd;
    FILE * resultfile;
    struct sockaddr_in address;
    char buffer[50];
    fd_set readfds;
    resultfile = fopen("/tmp/nginx_vs_apache.log", "a");
    //Заполняем наш массив сокетов нулями
    for (i = 0; i < max_clients; i++)  client_socket[i] = 0;
    if ( (master_socket = socket(AF_INET , SOCK_STREAM , 0)) == 0)  error("socket failed");
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );
    if (bind(master_socket, (struct sockaddr *)&address, sizeof(address)) < 0) error("bind failed");
    if (listen(master_socket, 3) < 0) error("listen");
    addrlen = sizeof(address);
    while (1) //В бесконечном цикле обрабатываем запросы
    {
        FD_ZERO(&readfds);
        FD_SET(master_socket, &readfds);
        max_sd = master_socket;
        for ( i = 0 ; i < max_clients ; i++)
        {
            sd = client_socket[i];
            if (sd > 0) FD_SET( sd , &readfds);
            if (sd > max_sd) max_sd = sd;
        }
        //Ждем событий на любом из интересующих нас сокетов
        activity = select( max_sd + 1 , &readfds , NULL , NULL , NULL);
        if ((activity < 0) && (errno != EINTR))  printf("select error");
        //Обработка нового соединения
        if (FD_ISSET(master_socket, &readfds))
        {
            if ((new_socket = accept(master_socket, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) error("accept");
            for (i = 0; i < max_clients; i++)
                if ( client_socket[i] == 0 ) { client_socket[i] = new_socket; break; }
        }

        //Читаем данные из каждого сокета, так как не знаем какие события заставил ОС дать нам CPU
        for (i = 0; i < max_clients; i++)
        {
            sd = client_socket[i];
            if (FD_ISSET( sd , &readfds))
            {
                if ((valread = read( sd , buffer, 1024)) == 0) { close( sd ); client_socket[i] = 0; }
                else
                {
                    buffer[valread] = '\0';
                    fprintf(resultfile, buffer);
                    fflush (resultfile);
                }
            }
        }
    }

    return 0;
}

// Сначала команде select мы указывали сокет 4 (смотрите в квадратных скобках). По /proc мы узнали, что 4й файл-дескриптор — это сокет с номером 42651147. По netstat мы узнали, что сокет с таким номером — это наш сокет в состоянии listen порта 2222. Как только мы подключились к этому сокету, ОС произвела tcp handshake с нашим telnet клиентом и установила новое соединение, о чем известила приложение через select. Наша программа получила процессорное время и начала обрабатывать пустой массив с соединениями. Увидев, что это новое соединение, мы запустили команду accept, зная, что она точно не заблокирует выполнение программы, так как соединение уже присутствует. То есть фактически мы используем тот же accept, только в неблокирующем режиме.

// [root@101host nginx_vs_apache]$ ./differ &
// [1] 44832
// [root@101host nginx_vs_apache]$ ps axuf | grep [.]/differ
// root     44832 0.0  0.0   4060   448 pts/0    S    22:47   0:00              \_ ./differ
// [root@localhost ]# strace -p 44832
// Process 44832 attached - interrupt to quit
// select(5, [4], NULL, NULL, NULL)        = 1 (in [4])

// accept(4, {sa_family=AF_INET, sin_port=htons(41130), sin_addr=inet_addr("127.0.0.1")}, [16]) = 5
// select(6, [4 5], NULL, NULL, NULL^C <unfinished ...>
// Process 44832 detached
// [root@localhost ]# ls -lh /proc/44832/fd
// итого 0
// lrwx------ 1 root root 64 Апр 19 00:26 0 -> /dev/pts/12
// lrwx------ 1 root root 64 Апр 19 00:26 1 -> /dev/pts/12
// lrwx------ 1 root root 64 Апр 19 00:21 2 -> /dev/pts/12
// l-wx------ 1 root root 64 Апр 19 00:26 3 -> /tmp/nginx_vs_apache.log
// lrwx------ 1 root root 64 Апр 19 00:26 4 -> socket:[42651147]
// lrwx------ 1 root root 64 Апр 19 00:26 5 -> socket:[42651320]
// [root@localhost ]# netstat -apeen | grep 42651147
// tcp        0      0 0.0.0.0:2222                0.0.0.0:*                   LISTEN      500        42651147   44832/./differ
// [root@localhost ]# netstat -apeen | grep 42651320
// tcp        0      0 127.0.0.1:2222              127.0.0.1:41130             ESTABLISHED 500        42651320   44832/./differ