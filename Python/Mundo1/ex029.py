# Escreva o programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 para cada km acima do limite.

velocidade = float(input('Qual a velocidade do veículo: '))

# uma estrutura condicional IF/ELSE sem o uso de ELSE é do tipo de condição simples
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('\n============== NOTIFICAÇÃO DE MULTA ================')
    print(f'Você excedeu o limite de velocidade em {velocidade-80:.1f} kms')
    print(f'E recebeu uma multa no valor de R$ {multa:.2f}')
    print('======================================================\n')

print('\n=======================================')
print('Tenha um bom dia e dirija em segurança')
print('=======================================\n')