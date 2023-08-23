def encaixa(A, B):
    str_A = str(A)
    str_B = str(B)
    
    if len(str_B) > len(str_A):
        return "não encaixa"
    
    if str_A[-len(str_B):] == str_B:
        return "encaixa"
    else:
        return "não encaixa"

# Número de vezes para realizar a verificação
N = int(input("Digite o valor de N: "))

for _ in range(N):
    A, B = map(int, input("Digite os valores de A e B: ").split())
    resultado = encaixa(A, B)
    print(resultado)
