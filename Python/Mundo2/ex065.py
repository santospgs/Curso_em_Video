# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e
# e qual foi o maior e o menor valor lido. O programa deve 
# perguntar ao usuário se ele quer ou não continuar a digitar valores

num = int(input('Informe um número inteiro: '))
soma = num
cont = 1
pergunta = None
lista_num = []

while pergunta != 'N':
    lista_num.append(num)
    pergunta = str(input('Deseja informar outro valor [s/n]? ')).strip().upper()

    if pergunta == 'S':
        num = int(input('Informe um número inteiro: '))
        soma += num
        cont += 1
        
#print(soma)
#print(cont)
media = soma / cont
print(f'A média dos valores é {media:.2f}')
#print(lista_num)
print(f'Menor valor: {min(lista_num)}')
print(f'Maior valor: {max(lista_num)}')

