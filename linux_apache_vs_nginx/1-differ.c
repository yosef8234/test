#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>

//Порт, который мы слушаем
#define PORT_NO 2222

int main(int argc, char *argv[])
{
    //Буфер, куда мы будем считывать данные из сокета
    long buffersize = 50;
    int sockfd, newsockfd;
    socklen_t clilen;
    // Переменная, в которой будет храниться адрес нашего буфера
    char *buffer;
    struct sockaddr_in serv_addr, cli_addr;
    FILE * resultfile;
    // выделяем память
    buffer = malloc (buffersize + 1);
    //открываем файл для записи наших сообщений
    resultfile = fopen("/tmp/nginx_vs_apache.log", "a");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    bzero(buffer, buffersize + 1);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(PORT_NO);
    //создаем структуру (сокет), тут SOCK_STREAM это tcp/ip сокет.
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) error("ERROR opening socket");
    //определяем структуру нашего сокета, будем слушать порт 2222 на всех ip адресах
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) error("ERROR on binding");
    // говорим нашей ОС, чтобы она принимала входящие коннекты для нашего сокета, максимум 50
    listen(sockfd, 50);
    while (1) {
        //в замкнутом цикле обрабатываем входящие подключения и читаем из них
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) error("ERROR on accept");
        read(newsockfd, buffer, buffersize);
        fprintf(resultfile, buffer);
        fflush (resultfile);
    }
    close(sockfd);
    return 0;
}

// [root@ localhost]# ps axuf | grep [d]iffer
// root      45409  0.0  0.0   4060   460 pts/12   S+   01:14   0:00  |   \_ ./differ
// [root@localhost ]# netstat -tlnp | grep 2222
// tcp        0      0 0.0.0.0:2222                0.0.0.0:*                   LISTEN      45409/./differ
// [root@localhost ]# ls -lh /proc/45409/fd
// итого 0
// lrwx------ 1 root root 64 Апр 19 01:16 0 -> /dev/pts/12
// lrwx------ 1 root root 64 Апр 19 01:16 1 -> /dev/pts/12
// lrwx------ 1 root root 64 Апр 19 01:16 2 -> /dev/pts/12
// l-wx------ 1 root root 64 Апр 19 01:16 3 -> /tmp/nginx_vs_apache.log
// lrwx------ 1 root root 64 Апр 19 01:16 4 -> socket:[42663416]
// [root@localhost ]# netstat -apeen | grep 42663416
// tcp        0      0 0.0.0.0:2222                0.0.0.0:*                   LISTEN      500        42663416   45409/./differ
// [root@localhost ]# strace -p 45409
// Process 45409 attached - interrupt to quit
// accept(4, ^C <unfinished ...>
// Process 45409 detached
// [root@localhost ]#