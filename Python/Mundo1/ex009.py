# Faça um programa que lei um número inteiro qualquer o mostre na tela sua tabuada

num = int(input('Informe um número: '))

print(f'===== TABUADA DO {num} =====')
for i in range(1,11):    
    print(f'{num} x {i:2} = {num*i:2}')