// Мы делаем accept, принимаем новое соединение. Далее мы запускаем fork. И если это мастер процесс (fork вернул pid созданного процесса), то мы закрываем текущее соединение в родительском процессе (оно доступно и в родителе, и в дочернем процессе). Если это дочерний процесс (fork вернул 0), то мы начинаем делать read с открытого сокета, который мы открыли командой accept в родительском процессе. По факту получается, что родительский процесс у нас только принимает соединения, а read/write мы делаем в дочерних процессах.

#include <stdio.h>
#include <string.h>
#include <netinet/in.h>

#define PORT_NO 2222

int main(int argc, char *argv[])
{
    int sockfd, newsockfd;
    socklen_t clilen;
    char buffer;
    char * pointbuffer = &buffer;
    struct sockaddr_in serv_addr, cli_addr;
    FILE * resultfile;
    int pid = 1;
    resultfile = fopen("/tmp/nginx_vs_apache.log", "a");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(PORT_NO);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) error("ERROR opening socket");
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) error("ERROR on binding");
    listen(sockfd, 50);
    while (pid != 0) {
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) error("ERROR on accept");
        pid = fork();
        if (pid != 0) {
            close(newsockfd);
            fprintf(resultfile, "New process was started with pid=%d\n", pid);
            fflush (resultfile);
        }
    }
    while (read(newsockfd, pointbuffer, 1)) {
        fprintf(resultfile, pointbuffer);
        fflush (resultfile);
    }
    close(sockfd);
    return 0;
}

// [root@localhost ]# ps axuf | grep [d]iffer
// root      45643  0.0  0.0   4060   504 pts/12   S+   01:40   0:00  |   \_ ./differ
// root      45663  0.0  0.0   4060   156 pts/12   S+   01:41   0:00  |       \_ ./differ
// root      45665  0.0  0.0   4060   160 pts/12   S+   01:41   0:00  |       \_ ./differ

// Клиент1:
// [root@localhost ]$ telnet localhost 2222
// Connected to localhost.
// Escape character is '^]'.
// client 1 test
// megatest

// Клиент2:
// [root@localhost ]$ telnet localhost 2222
// Connected to localhost.
// Escape character is '^]'.
// client2 test
// yoyoyoy

// [root@localhost ]# cat /tmp/nginx_vs_apache.log
// New process was started with pid=44163
// New process was started with pid=44165
// client 1 test
// megatest
// client2 test
// yoyoyoy