#include <stdio.h>

int main(void)
{
    char word[21] ={""};
    scanf("%s",word);
    for(int i = 0; i< 20; i++)
    {
        if(word[i] != "") printf("\'%c\'\n",word[i]);
    }
    return 0;
}