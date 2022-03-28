# A confederação nacional de natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade:
#
# até 9 anos - mirim
# até 14 anos - infantil
# até 19 anos - junior
# até 20 anos - senior
# acima - master
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Informe seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} ano(s)")
if(idade <= 9):
    print ("Categoria MIRIM")
elif(idade <= 14):
    print ("Categoria INFANTIL")
elif (idade <= 19):
    print ("Categoria JUNIOR")
elif (idade <= 20):
    print ("Categoria SÊNIOR")
else:
    print ("Categoria MASTER")