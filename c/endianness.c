#include <fcntl.h>
#include <unistd.h>

int main() {
   int i = 0xdeadbeef;
   int fd;

   fd = open("endianness.dat", O_WRONLY | O_CREAT, 0700);
   write(fd, &i, sizeof(int));
   close(fd);

   return 0;
}

/*
# On macOS:
smm@Cortene c % hexdump endianness.dat
0000000 beef dead
0000004
smm@Cortene c % hexdump -C endianness.dat
00000000  ef be ad de                                       |....|
00000004
*/
