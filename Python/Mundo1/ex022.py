### Criei um programa que leia o nome completo de uma pessoa e mostre:
### - o nome com todas as letras maíusculas
### - o nome com todas as letras minúsculas
### - quantas letras ao todo (sem considerar espaços)
### - quantas letras tem o primeiro nome

nome = str(input('Informe seu nome completo: ')).strip()

### DIVIDIR O NOME NUMA LISTA
nome_dividido = nome.split()

### REMOVER ESPAÇOS
nome_completo = len(nome.replace(' ',''))
# nome_completo = len(''.join(nome))
# nome_completo = len(nome) - nome.count(' ')

print(f'\n- maiúsculo: {nome.upper()}')
print(f'- minúsculo: {nome.lower()}')
print(f"- O nome completo tem {nome_completo} letras")
print(f'- O primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras\n')
