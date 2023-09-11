N = int(input())

v = []

for i in range(N):
    v = input().split(" ")
    A = v[0]
    B = v[1]

    if len(B) > len(A):
        print("não encaixa")
    elif A.endswith(B):
        print("encaixa")
    else:
        print("não encaixa")