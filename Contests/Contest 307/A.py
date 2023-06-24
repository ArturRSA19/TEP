def calcular_passos_semanais(N, A):
    passos_semanais = []
    soma_semanal = 0
    semana_atual = 1
    
    for passos in A:
        soma_semanal += passos
        
        if semana_atual == 7:
            passos_semanais.append(soma_semanal)
            soma_semanal = 0
            semana_atual = 1
        else:
            semana_atual += 1
    
    # Verifica se sobraram dias na última semana 
    if soma_semanal > 0:
        passos_semanais.append(soma_semanal)
    
    return passos_semanais


N = int(input())
A = list(map(int, input().split()))
resultado = calcular_passos_semanais(N, A)
print(*resultado)
