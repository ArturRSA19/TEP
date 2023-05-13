from math import *

a, b, c = map(int, input().split())

if a < 0:
    b = -b
    c = -c
    a = -a

delta = b*b - 4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        print(1)
        print("%.5f" % (-c*1.0/b))
elif delta == 0:
    print(1)
    print("%.5f" % (-b/(2*a)))
elif delta > 0:
    print(2)
    print("%.5f" % ((-b-sqrt(delta))/(2*a)))
    print("%.5f" % ((-b+sqrt(delta))/(2*a)))
else:
    print(0)