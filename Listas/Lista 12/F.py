n1, n2, k1, k2 = map(int, input().split())

while(n1>0 or n2>0):
    n1 -= 1
    n2 -= 1
    if(n1 == n2):
        print("Second")
        break
    if(n2 <= 0):
        print("First")
        break
    if(n1 <= 0):
        print("Second")
        break