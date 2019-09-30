#include <stdio.h>

void update(int *a,int *b) {
    int a_cp = *a;
    int b_cp = *b;
    *a = a_cp + b_cp;
    *b = a_cp > b_cp ? a_cp - b_cp : b_cp - a_cp;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
