'''
flag (Bandeira) - marcar local
None = Não valor
is e is not = é ou não é (tipo , valor, identidade)
id = identidade

'''

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
   
    print('não faça nada')


if passou_no_if is None:
    print('não passou no if')

else:
    print('passou no if')