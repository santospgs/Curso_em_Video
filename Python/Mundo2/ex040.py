# Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
#
# Média < 5.0 - Reprovado
# Média >= 5.0 e <= 6.9 - Recuperação
# Média > 7.0 Aprovado

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

print(media)

if (media < 5):
    print("Aluno reprovado")
elif (media >= 5 and media < 7):
    print("Recuperação")
else:
    print("Aluno aprovado!")