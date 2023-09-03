N = int(input())



while N > 0:
    A = input()
    B = input()
    if A not in B:
        print("não encaixa")
    else:
        print("encaixa")
    N +=1


# for i in range(N):
#     while len(A) != len(B):
#         print("não encaixa")
#     else:
#         print("encaixa")