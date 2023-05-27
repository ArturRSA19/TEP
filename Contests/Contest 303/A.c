#include <stdio.h>
#include <string.h>

int main(){
    int aux = 0;
    int n;
    scanf("%d\n", &n);
    
    char s[n+1], t[n+1];

    scanf("%s", s);
    scanf("%s", t);

    for(int i = 0; i<n; i++){
        if(s[i] == t[i]){
            aux++;
        } else if((s[i] == 'o') && (t[i] == '0') || (t[i] == 'o') && (s[i] == '0')){
            aux++;
        } else if((s[i] == 'l') && (t[i] == '1') || (s[i] == '1') && (t[i] == 'l')){
            aux++;
        }
    }

    if(aux == n){
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}