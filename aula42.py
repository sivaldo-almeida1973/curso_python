texto = 'Python s2'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
  print(texto[i], i)


  i += 1

print('-' *30)

senha_salva = '123456'
senha_digitada = ''
repetições = 0


while senha_salva != senha_digitada:
  senha_digitada = input(f'sua senha ({repetições}X): ')

  repetições += 1

print(repetições)
print('Aquele laço acima pode ter repetições infinitas')


print('-' *30)
#Introdução ao for(para)/in-estrutura de repetições para coisas finitas

texto = 'python'


for letra in texto:
  print(letra, letra * 10)

  