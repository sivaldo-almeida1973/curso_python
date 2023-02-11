"""
Faça um programa que peça o primeiro nome do usuário .Se o
nome tiver 4 letras ou menos ecreva "seu nome é curto"; se
tiver entre 5 e 6 letras, escreva " seu nome é normal";
maior que 6 escreva "seu nome é muito grande".


"""
nome = input('Digite se primeiro nome: ')

if len(nome) <= 4:
  print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <=6:
  print('Seu nome é normal')
elif len(nome) > 6:
 print('Seu nome é muito grande')
else:
  print('Digite mais de uma letra!')
