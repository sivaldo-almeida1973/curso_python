'''
CONSTANTE = 'variáveis' que não vão mudar
Muitas condições no mesmo if é (ruim)
....<- Contagem de complexidade (ruim)
'''
velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que ocarro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 =  local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if velocidade > RADAR_1:
    print('Velocidade carro ultrapassou no radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

else:
    print('carro abaixo da velocidade do radar 1')
print('dirija com cuidado!!')


