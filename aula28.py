"""
Exercício
Peça ao usuario para digitar seu noome
Peça ao usuario para digitar sua idade
Se o nome e a idade forem digitados :
 ....Exiba:
 .........Seu nome é {nome}
 .........seu nome invertido é {nome invertido}
 .........Se o nome contém (ou não) espaços
 .........Se nome tem {n} letras
 .........A primeira letra do seu nome é {letra}
 .........A ultima letra do seu nome é {letra}
 Se nada for digitado em nome ou idade:
 ...Exiba 'Desculpe , você deixou campos vazios.
"""
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome and idade :
    print(f'seu nome é {nome} ')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome não contém espaços')

    print(f'seu nome tem {(len(nome))} letras ')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe , voce deixou campos vazios. ")
