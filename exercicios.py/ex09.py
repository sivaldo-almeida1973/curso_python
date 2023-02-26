#Crie uma lista de compras com listas, o usuario deve ter #a possibilidade de inserir ,apagar e listar valores da #sua lista .Não permita que o programa quebre com erros #de indices ixexistentes na lista.
import os 
lista = []

while True:
    print('selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar:')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor:')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar:')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite numero int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('ERRO desconhecido.')
    elif opcao == 'l':
        os.system('clear')

        if len(lista)  == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('por favor , escolha i, a, ou l.')