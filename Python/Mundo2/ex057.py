# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores M e F. Caso esteja errado, peça a digitação novamente
# até obter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

#while (sexo != 'F') and (sexo != 'M'):
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite novamente: ')).strip().upper()[0]

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'    
print(f'\nSexo {sexo}. Ok, tudo certo')
