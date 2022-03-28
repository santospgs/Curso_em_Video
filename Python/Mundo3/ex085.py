# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares
# e impares. No final, mostre os valores pares e impares em ordem crescente.

valores = [[],[]]

for n in range(1, 8):
    num = int(input(f'Valor {n}: '))
    if num % 2 == 0:
        for c, v in enumerate(valores[0]):
            if num < v:
                valores[0].insert(c, num)
                break
        else:
            valores[0].append(num)        
    else:
        for c, v in enumerate(valores[1]):
            if num < v:
                valores[1].insert(c, num)
                break
        else:
            valores[1].append(num)          
print(valores)


'''if n == 1 or num > valores[1][-1]:
            valores[1].append(num)
        else:
            pos = 0
            while pos < len(valores[1]):
                if num <= valores[1][pos]:
                    valores[1].insert(pos, num)
                    break
                pos += 1'''