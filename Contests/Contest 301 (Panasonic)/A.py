n = int(input())
s = str(input())
contT = 0
contA = 0

for letra in s:
    if(letra == 'T'):
        contT+=1
    elif(letra == 'A'):
        contA+=1

if(contT == contA):
    if(s[-1]=='A'):
        print('T')
    elif(s[-1]=='T'):
        print('A')
elif(contT > contA):
    print('T')
elif(contA > contT):
    print('A')


