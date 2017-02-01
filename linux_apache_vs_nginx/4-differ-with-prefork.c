#include <stdio.h>
#include <string.h>
#include <netinet/in.h>

#define PORT_NO 2222

int main(int argc, char *argv[])
{
    int sockfd, newsockfd, startservers, count ;
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
    startservers = 2;
    count = 0;
    while (pid != 0) {
        if (count < startservers)
        {
            pid = fork();
            if (pid != 0) {
                close(newsockfd);
                fprintf(resultfile, "New process was started with pid=%d\n", pid);
                fflush (resultfile);
            }
            count = count + 1;
        }
        //sleep (1);
    }
    newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
    if (newsockfd < 0) error("ERROR on accept");
    while (read(newsockfd, pointbuffer, 1)) {
        fprintf(resultfile, pointbuffer);
        fflush (resultfile);
    }
    close(sockfd);
    return 0;
}

// [root@localhost ]# ps axuf | grep [d]iffer
// root      44194 98.0  0.0   4060   504 pts/12   R+   23:35   0:07  |   \_ ./differ
// root      44195  0.0  0.0   4060   152 pts/12   S+   23:35   0:00  |       \_ ./differ
// root      44196  0.0  0.0   4060   156 pts/12   S+   23:35   0:00  |       \_ ./differ

// [root@localhost ]# top -n 1 | head
// top - 23:39:22 up 141 days, 21 min,  8 users,  load average: 1.03, 0.59, 0.23
// Tasks: 195 total,   2 running, 193 sleeping,   0 stopped,   0 zombie
// Cpu(s):  0.3%us,  0.2%sy,  0.0%ni, 99.3%id,  0.2%wa,  0.0%hi,  0.0%si,  0.0%st
// Mem:   1896936k total,  1876280k used,    20656k free,   151208k buffers
// Swap:  4194296k total,   107600k used,  4086696k free,  1003568k cached

//     PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
//   44194 root     20   0  4060  504  420 R 98.9  0.0   4:10.54 differ
//   44255 root      20   0 15028 1256  884 R  3.8  0.1   0:00.03 top
//       1 root      20   0 19232  548  380 S  0.0  0.0   2:17.17 init

// [root@localhost ]# strace -p 44194
// Process 44194 attached - interrupt to quit
// ^CProcess 44194 detached
// [root@localhost ]#

// [root@localhost ]# strace -p 44195
// Process 44195 attached - interrupt to quit
// accept(4, ^C <unfinished ...>
// Process 44195 detached
// [root@localhost ]# strace -p 44196
// Process 44196 attached - interrupt to quit
// accept(4, ^C <unfinished ...>
// Process 44196 detached

// [root@localhost ]$ telnet localhost 2222
// Connected to localhost.
// Escape character is '^]'.
// client 1 test
// hhh

// [root@localhost ]# strace -p 44459
// Process 44459 attached - interrupt to quit
// read(5, ^C <unfinished ...>
// Process 44459 detached
// [root@localhost ]# strace -p 44460
// Process 44460 attached - interrupt to quit
// accept(4, ^C <unfinished ...>
// Process 44460 detached

// // if uncomment sleep()

// [root@localhost ]# strace -p 44601
// …..
// rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
// rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
// rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
// nanosleep({1, 0}, 0x7fff60a15aa0)       = 0
// ….
// rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
// rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
// rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
// nanosleep({1, 0}, 0x7fff60a15aa0)        = 0
// …

// // the same as httpd with prefork

// [root@www /]# ps axuf | grep [h]ttpd
// root     12730  0.0  0.5 271560 11916 ?        Ss   Feb25   3:14 /usr/sbin/httpd
// apache   19832  0.0  0.3 271692  7200 ?        S    Apr17   0:00  \_ /usr/sbin/httpd
// apache   19833  0.0  0.3 271692  7212 ?        S    Apr17   0:00  \_ /usr/sbin/httpd
// apache   19834  0.0  0.3 271692  7204 ?        S    Apr17   0:00  \_ /usr/sbin/httpd
// apache   19835  0.0  0.3 271692  7200 ?        S    Apr17   0:00  \_ /usr/sbin/httpd

// [root@www /]# strace -p 19832
// Process 19832 attached
// accept4(3, ^CProcess 19832 detached
//  <detached ...>
// [root@www /]# strace -p 19833
// Process 19833 attached
// accept4(3, ^CProcess 19833 detached
//  <detached ...>

//  [root@www /]# strace -p 12730
// Process 12730 attached
// select(0, NULL, NULL, NULL, {0, 629715}) = 0 (Timeout)
// wait4(-1, 0x7fff4c9e3fbc, WNOHANG|WSTOPPED, NULL) = 0
// select(0, NULL, NULL, NULL, {1, 0})     = 0 (Timeout)
// wait4(-1, 0x7fff4c9e3fbc, WNOHANG|WSTOPPED, NULL) = 0
// select(0, NULL, NULL, NULL, {1, 0})     = 0 (Timeout)
// wait4(-1, 0x7fff4c9e3fbc, WNOHANG|WSTOPPED, NULL) = 0