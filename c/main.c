#include <stdio.h>

int main(void)
{
    char word[100] = {0};
    scanf("%s", &word);
    char alpha;
    
    for(alpha = 0x61; alpha <= 0x7a; alpha++)
    {
        for(int i = 1; i <= 100; i++)
        {
            if(word[i] == 0)
            {
                break;
            }
            if(alpha == word[i])
            {
                printf("%d ", i);
            }
        }
    }
    return 0;
}