#include <stdio.h>

void my_int_func(int x)
{
    printf("%d\n", x);
}

int main()
{
    void (*x)(int);
    x = &my_int_func;
    x(2);
    (*x)(2);

    return 0;
}


