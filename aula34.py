"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""
condicao = True


while True:
    nome = input('qual o seu nome: ')
    print(f'seu nome é :  { nome}  ')

    if nome == 'sair':
        break

print('acabou')
    

