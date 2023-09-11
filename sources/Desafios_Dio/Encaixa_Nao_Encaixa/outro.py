N = int(input())

for i in range(N):
    A = input()
    B = input()
    A2 = int(len(A))
    B[-A2:]
  
    if A == B[-A2:]:
        print('encaixa')
    else:
        print('não encaixa')