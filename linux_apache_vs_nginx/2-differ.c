// Программа с бесконечным чтением из сокета

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
    resultfile = fopen("/tmp/nginx_vs_apache.log", "a");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(PORT_NO);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) error("ERROR opening socket");
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) error("ERROR on binding");
    listen(sockfd, 50);
    while (1) {
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) error("ERROR on accept");
        while (read(newsockfd, pointbuffer, 1)) {
            fprintf(resultfile, pointbuffer);
            fflush (resultfile);
        }
    }
    close(sockfd);
    return 0;
}