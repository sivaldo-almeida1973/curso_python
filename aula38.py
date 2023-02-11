"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condiçõa for verdadeira

Loop infinito -> Quando um codigo não tem fim
"""

qtd_linhas = 5 #condição
qtd_colunas = 5

linha  = 1  #contador

while linha <= qtd_linhas:
  coluna = 1

  print(linha)

  while coluna <= qtd_colunas:
    print(f'{linha=} {coluna=}')
    coluna += 1
  linha += 1

print('Acabou')
