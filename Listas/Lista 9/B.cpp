#include <iostream>
#include <cmath>
using namespace std;

unsigned long long bigmod(unsigned long long B, unsigned long long P, unsigned long long  M)
{
    if(P == 1)
        return B%M;
    else if(P%2 == 0)
        return (bigmod(B,P/2,M)*bigmod(B,P/2,M))%M;
    else
        return (bigmod(B, 1, M)*bigmod(B, (P-1)/2, M)*bigmod(B, (P-1)/2, M))%M;
}

int main(void)
{
    unsigned long long B = 0, P = 0, M = 0;
    unsigned long long ans = 0, partialmod = 0;
    ans = 1;
    while(cin >> B >> P >> M)
    {
        partialmod = B%M;
        ans = 1;
        for (unsigned long long  i = 0; i < 64; i++)
        {
            if(i != 0)
                partialmod = (partialmod*partialmod)%M;
            if(((P>>i)&1) == 1)
                ans = (ans*partialmod)%M;
        }
        cout << ans << endl;
    }
    return 0;
}

