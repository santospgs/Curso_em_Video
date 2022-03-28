# Crie um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente
#-----
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome_completo = str(input('Qual seu nome completo: ')).strip()

nome_split = nome_completo.split()

print(f'O primeiro nome é: {nome_split[0]}')
print(f'O último nome é: {nome_split[-1]} ')