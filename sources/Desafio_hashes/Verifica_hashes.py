def verificar_hash(lista_hashes):
    for hash_comparacao in lista_hashes:
        hash_calculado, hash_esperado = hash_comparacao.split(',')

        if hash_calculado == hash_esperado:
            print('Correto')
        else:
            print('Inválido')

    return


hashes_usuario = []
hashes_usuario = input().strip()
lista_hashes = hashes_usuario.split(';')

verificar_hash(lista_hashes)
