# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições pescisam ser 
# verdadeiras.

# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São consideradas falsy (que vc já)
# (0 0.0 '' False)
# Tambem existe o tipo (None) que é
# usado para representar um (não valor)

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')


#senha_permitida = '123456'
#
#if (entrada == 'E' or entrada == "e" )and #senha_digitada == senha_permitida:
# #   print('Entrar')
#else:
#    print('Sair')

# Avaliação de curto cicuito

senha = input('senha: ') or 'sem senha'
print(senha)
