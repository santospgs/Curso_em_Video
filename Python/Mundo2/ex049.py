# refaça o exercício 009 monstrando a tabuada de um 
# numero que o usuario escolher, utilizando o laço FOR

num = int(input('Informe um número'))

for n in range (1,11):
    print(f'{num} x {n} = {num*n}')