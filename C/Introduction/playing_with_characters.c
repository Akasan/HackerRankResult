#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch[100], s[100], sen[100];
    scanf("%[^\n]%*c", ch);
    scanf("%[^\n]%*c", s);
    scanf("%[^\n]%*c", sen);

    printf("%s\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}
