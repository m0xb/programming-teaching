#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s <file>\n", argv[0]);
        return 1;
    }

    int fd;
    int buf;

    fd = open(argv[1], O_RDONLY);
    printf("Reading an int from the file...\n");
    read(fd, &buf, sizeof buf);
    close(fd);
    printf("First int: %x\n", buf);
    printf("bytes[0]: %x\n", buf & 0xFF);
    printf("bytes[1]: %x\n", (buf >> 8) & 0xFF);
    printf("bytes[2]: %x\n", (buf >> 16) & 0xFF);
    printf("bytes[3]: %x\n", (buf >> 24) & 0xFF);

    printf("Reading four bytes from the file...\n");
    buf = 0;
    fd = open(argv[1], O_RDONLY);
    for (int i = 0; i < 4; ++i) {
        read(fd, &buf, 1);
        printf("bytes[%d]: %x\n", i, buf);
    }
    close(fd);

    return 0;
}
