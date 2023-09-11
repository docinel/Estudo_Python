# import pyautogui as pa
# entrada = pa.prompt(text='Digite a quantidade:', title='TESTE' , default='')


# pa.alert(text= entrada[3::], title='RESPOSTA', button='OK')

A = '123123'
print(A[-1])

N = int(input())

for i in range(N):
    A, B = list(map(str, input().split()))
    A2 = int(len(A))
    B[-A2:]
  
    if A == B[-A2:]:
        print('encaixa')
    else:
        print('não encaixa')