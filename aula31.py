"""
CONSTANTE = "Variável" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # VELOCIDADE MÁXIMA DO RADAR 1
LOCAL_1 = 100  # local onde o radar 1 está
RANDAR_RANGE = 1  # A distância onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RANDAR_RANGE) and \
    local_carro <= (LOCAL_1 + RANDAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1


if vel_carro_passou_radar_1:
    print('O carro passou acima da velocidade no radar1')

if carro_passou_radar_1:
    print('O carro passou no radar1')

if carro_multado_radar_1 and vel_carro_passou_radar_1:
    print('carro multado em radar 1')
