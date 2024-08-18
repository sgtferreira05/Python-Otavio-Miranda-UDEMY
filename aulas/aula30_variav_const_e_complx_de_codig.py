'''
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condições no mesmo if (PÉSSSSSSSIMO)
    <- Contagem de complexidade (RUIMMM)
'''

velocidade = 61 #Velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distância onde o radas pega

vel_car_pass_radar_1 = velocidade > RADAR_1
car_mult_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and\
      local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_car_pass_radar_1 :
    print('O carro passou acima da velocidade permitida.')

if  car_mult_radar_1 and vel_car_pass_radar_1:
    print('Carro Multado no radar 1')