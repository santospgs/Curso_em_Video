# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

#### MINHA SOLUÇÃO ####
'''primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
enezimo = termo + (11 - 1) * razao

while termo < enezimo:
    print(f'{termo}',end=' -> ')  
    termo += razao   
print('FIM!')
'''
#### SOLUÇÃO DO VÍDEO ###$
primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}',end=' -> ')
    termo += razao
    cont += 1    
print('FIM!')