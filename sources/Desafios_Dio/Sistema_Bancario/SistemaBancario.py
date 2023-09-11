# Operações:
    # Depósito
    # Saque
    # Extrato

limite = 500
deposito = 0
saldo = deposito
saque = 0
numero_saque = 0
LIMITE_SAQUE = 3
extrato = 0


menu = '''
[d] Depositar
[s] Saldo
[e] Extrato
[q] Sair

'''
while True:
    opcao = input(menu)
    if opcao == 'd':
        deposito = int(input('Quanto você gostaria de depositar? '))
        
    if opcao == 's':
        print(f'R${saldo}')
    if opcao == 'e':
        print('Extrato')
    elif opcao == 'q':
        break
    else:
        print('Opção inválida')


