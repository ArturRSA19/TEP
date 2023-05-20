#include <stdio.h>

int main(){

    unsigned long long x, y, z, aux, intervalo;
    scanf("%lld %lld %lld", &x, &y, &z);

    intervalo = y-x;
    printf("%lld", intervalo/z);

    return 0;
}