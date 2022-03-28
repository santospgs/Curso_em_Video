# Desenvolva uma la que leia o peso e a altura da pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - abaixo de 18.5 - abaixo do peso
# - entre 18.5 e 25 - peso ideal
# - 25 ate 30 - sobrepeso
# - 30 ate 40 - obesidade
# - acima de 40 - obesidade morbida

peso = float(input("Qual seu peso? (Kg): ").replace(",","."))
altura = float(input("Qual a sua altura? (m): ").replace(",","."))

imc = peso/(altura ** 2) #para se usar potencias utiliza-se ** o invés de ^

print("-"*20)
print(f"Seu peso peso é {peso:.2f} Kg")
print(f"Sua altura altura é {altura:.2f} m")
print(f"Seu IMC é {imc:.2f}")
print("-"*20)

if (imc < 18.5):
    print ("Abaixo do peso")
elif (imc >= 18.5 and imc < 25):
    print ("Peso ideal")
elif (imc >= 25 and imc < 30):
    print ("Sobrepeso")
elif (imc >= 30 and imc < 40):
    print ("Obesidade")
else:
    print ("Obesidade morbida")