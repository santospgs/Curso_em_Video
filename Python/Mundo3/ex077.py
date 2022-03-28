# Crie um programa que tenha uma tupla com várias palavras (sem acentos).
# Depois disso você deve mostrar quais são suas vogais.
vogais = ('a','e','i','o','u')
palavras = ('Censura','Caminho','Diariamente','Capricho','Azul','Artista','Eternidade','Ursinho')

# ------------ SOLUÇÃO GUANABARA ------------
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')


# ------------ MINHA SOLUÇÃO ------------
'''
for i in range(len(palavras)):
    palavra = tuple(palavras[i].lower())
    print(f'As vogais da palavra \033[4m{palavras[i].upper()}\033[m são: ',end='')
    for vogal in range(len(palavra)):
        if palavra[vogal] in vogais:
            print(palavra[vogal],end=' ')
    print()
    print('-'*40)
'''



