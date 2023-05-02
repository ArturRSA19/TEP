a, b, c, d = [int(x) for x in input().split()]

if(a>=c and (a-c) <= d):
    print('Yes')
elif(c>=a and (c-a) <= d):
    print('Yes')
elif(a>=b and a-b<=d and b>=c and b-c<=d):
    print('Yes')
elif(b>=a and b-a<=d and c>=b and c-b<=d):
    print('Yes')
else:
    print('No')