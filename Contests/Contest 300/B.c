#include <stdio.h>

int main(){

    int H, W;

    scanf("%d %d", &H, &W);

    char A[H][W], B[H][W];

    for(int i = 0; i<H; i++){
        for(int j = 0; j<W; i++){
            scanf("%c", &A[i][j]);
        }
    }

    for(int i = 0; i<H; i++){
        for(int j = 0; j<W; i++){
            scanf("%c", &B[i][j]);
        }
    }

    return 0;

}