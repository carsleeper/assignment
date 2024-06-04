#include <stdio.h>

int main(void)
{
    float x;
    scanf("%f",&x);
    int N = x/1;
    float M = x-N;
    printf("%d\n%f",N,M);
    return 0;
}