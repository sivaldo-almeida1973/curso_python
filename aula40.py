"""
while/else
"""
string = 'Valor qualquer'

i = 0
while i < len(string):#checando se indice é menor que o tamanho da str
  letra = string[i] # pegando cada uma das letras da str

  print(letra)  #imprimindo
  i += 1  # e somando mas 1 no indice

else:
  print('O else foi executado.')

print('Fora do while.')



print('-'*30)
string = 'Valor qualquer'

i = 0
while i < len(string):#checando se indice é menor que o tamanho da str
  letra = string[i] # pegando cada uma das letras da str

  if letra == ' ':#suponha que queira achar espaço vazio
    break
    
  print(letra)  #imprimindo
  i += 1  # e somando mas 1 no indice

else:
  print('O else foi executado.')

print('o else não sera executado por causa do break')
print('Fora do while.')