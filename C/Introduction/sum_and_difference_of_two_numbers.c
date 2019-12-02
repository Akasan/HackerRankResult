#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a1, b1;
    float a2, b2;

    scanf("%d %d", &a1, &b1);
    scanf("%f %f", &a2, &b2);

    printf("%d %d\n", a1+b1, a1-b1);
    printf("%.1f %.1f\n", a2+b2, a2-b2);

    return 0;
}


