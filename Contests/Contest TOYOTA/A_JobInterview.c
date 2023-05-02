#include <stdio.h>

int main(){

    int N;
    scanf("%d", &N);

    char S[N];
    scanf("%s", S);

    int i;
    int contador_o = 0; //contador para contar quatidade de Goods
    int contador_x = 0; //contador para contar quatidade de Poors

    for(i = 0; i < N; i++){

        if( S[i] == 'x' ){ 
            contador_x++;
            break;
        } else if ( S[i] == 'o'){
            contador_o++;
        }
    }

    if((contador_x == 0) && (contador_o >= 1)){
        printf("Yes");
    } else {
        printf("No");
    }

    return 0;

}