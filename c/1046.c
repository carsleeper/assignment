#include <stdio.h>

int main(void)
{
    long long n,m,k;
    scanf("%lld %lld %lld",&n ,&m ,&k);
    printf("%lld\n%.1f",n+m+k ,(float)(n+m+k)/3 );
    return 0;
}