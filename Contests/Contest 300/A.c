#include <stdio.h>

int main(){

    int N, A, B, soma;

    scanf("%d %d %d", &N, &A, &B);
    int C[N];
    soma = A+B;

    for(int i = 0; i<N; i++){
        scanf("%d", &C[i]);
    }

    for(int j = 0; j<N; j++){
        if(C[j] == soma){
            printf("%d\n", j+1);
        }
    }

    return 0;

}