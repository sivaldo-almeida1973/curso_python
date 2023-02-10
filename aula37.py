nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome and idade :
  print(f'seu {nome=}') 
  print(f'seu nome invertido é {nome[:: -1]}')

  if ' ' in nome:
   print(f'seu nome Contem espaços')
  else:
   print(f'seu nome Não contem espaços')

   print(f'seu nome tem{ (len(nome))} letras')
   print(f'A primeira letra do seu nome é:{nome[0]}')
   print(f'A ultima letra do seu nome é:{nome[-1]}')

  