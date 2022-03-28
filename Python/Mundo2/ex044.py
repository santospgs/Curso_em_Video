# Elabore um programa que calcule o valor a ser pago por um
# produto, considere o seu preço normal e condição de pagamento
# a vista (dinheiro/cheque): 10% de desconto
# a vista no cartão: 5% desconto
# até 2x no cartão: preço normal
# 3x ou mais: 20% de juros

valor = float(input("Qual o valor do produto?: "))

print ("-"*20)
print ("Como gostaria de pagar?")
print ("Opção 1 - a vista (Dinheiro)")
print ("Opção 2 - a vista (Cartão)")
print ("Opção 3 - 2x no cartão")
print ("Opção 4 - 3x ou mais")
print ("-"*20)
opcao = int(input("Digite a opção: "))

if (opcao == 1):
    print ("Pagamento a vista no dinheiro")
    print ("Desconto de 10%")
    valor = valor*0.9
elif (opcao == 2):
    print ("Pagamento a vista no cartão")
    print ("Desconto de 5%")
    valor = valor*0.95
elif (opcao == 3):
    print ("Pagamento em 2x no cartão")
    print ("Nenhum desconto")
    print (f"O valor da parcela será R$ {valor/2:.2f}")
elif (opcao == 4):
    print ("Pagamento em mais de 3x")
    print ("Juros de 20%")
    totalparc = int(input ("Qual a quantidade de parcelas: "))
    valor = valor * 1.2
    print (f'''A quantidade de parcelas é {totalparc}
    e o valor de cada parcela será R$ {valor/totalparc}''')
else:
    print("Opção inválida!")

print (f"Você irá pagar R$ {valor:.2f}")