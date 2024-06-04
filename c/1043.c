#include <stdio.h>

int main(void)
{
    long n;
    long m;
    scanf("%ld %ld",&n,&m);
    long mod = n%m;
    printf("%ld", mod);
    return 0;
}