#include <stdio.h>

int main()
{
    int n, i, nAtual, nAnterior = 0;
    int d, passosParaAdd, numMinMovimentos = 0;
    scanf("%d %d",&n, &d);

    for(i = 1; i <= n; i++)
    {
        scanf("%d",&nAtual);
        if(nAnterior >= nAtual)
        {
            passosParaAdd = (nAnterior - nAtual + 1)/d;
            passosParaAdd += (nAnterior - nAtual + 1)%d == 0 ? 0 : 1;

            nAtual = nAtual + passosParaAdd*d;
            numMinMovimentos += passosParaAdd;
        }
        nAnterior = nAtual;
    }

    printf("%d\n",numMinMovimentos);
    return 0;
}