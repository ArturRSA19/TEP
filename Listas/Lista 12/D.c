#include <stdio.h>

int main() {
    long long int A, B, K;
    scanf("%lld %lld %lld", &A, &B, &K);

    if (A >= K) {
        A -= K;
    } else {
        K -= A;
        A = 0;
        if (B >= K) {
            B -= K;
        } else {
            B = 0;
        }
    }

    printf("%lld %lld\n", A, B);
    return 0;
}
