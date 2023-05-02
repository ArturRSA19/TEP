x = str(input())

x = dict.fromkeys(x) #Remove as repetidas

aux = len(x) #Pega o tamanho da string

if(aux%2 == 0): #Se for par
    print("CHAT WITH HER!")
else: #Se for impar
    print("IGNORE HIM!")
