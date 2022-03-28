# Crie um programa onde o usuário possa digitar cinco valores e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# No final mostre a lista ordenada na tela

# SOLUÇÃO GUANABARA
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'A lista ordenada é {lista}')

# MINHA SOLUÇÃO
'''valores = []

for n in range(0,5):
    valor = int(input('Digite um valor: '))
    if len(valores) != 0:
        for c, v in enumerate(valores):
            if valor < v:
                valores.insert(c,valor)
                break
    else:
        valores.append(valor)
print(valores)'''

#########

'''valores = []

for i in range(0,5):
    valor = int(input('Digite um valor: '))

    for c, n in enumerate(valores):
        if valor < n:
            valores.insert(c,valor)
            break
    else:
        valores.append(valor)
            
print(valores)'''

    
    