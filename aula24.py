# Oeradores in (entre) e not in(não esta entre)
# strings são iteráveis
# 0 1 2 3 4 5
# o t á v i O
# -6-5-4-3-2-1
#nome = "sivaldo"
#print(nome[3])
#print(nome[-3])

#print("a" in nome)
#print('c' in nome)
#print(10 * '-')
#print('d' not in nome)
#print('f' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome} ')
else:
    print(f'{encontrar} não está em {nome}' )
