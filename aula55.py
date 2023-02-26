"""
Split e JOIN com list e str
split - divide uma string (metodo)
Join - une uma string

lstrip (corta espaços da esquerda)
rstrip (corta espaços da direita)
strip (corta espaços no começo e no fim)
"""

frase = 'Olha só que , coisa interessante'
lista_frases = frase.split(', ')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
print(lista_frases)


print('='*20)
frase = 'Olha só que , coisa interessante'
lista_frases = frase.split(', ')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].lstrip())
print(lista_frases)


print('='*20)
frase = 'Olha só que , coisa interessante'
lista_frases = frase.split(', ')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
print(lista_frases)



#alterar indice e imprime ass duas listas
print('='*20)
frase = 'Olha só que , coisa interessante'
lista_frases_crua = frase.split(', ')


lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())

print(lista_frases_crua)
print(lista_frases)


print('='*20)
#JOIN
frases_unidas = '='.join('abcd')
print(frases_unidas)