# Crie um programa que leia uma frase e informe quantas vezes aparece a letra A
# em que posição ela aparece pela primeira vez
# em que posição ela aparece pela ultima vez

frase = str(input('Informe uma frase qualquer: ')).strip().upper()
letra = str(input('Qual letra vc deseja contar? ')).strip().upper()

print(f"A letra '{letra}', aparece {frase.count(letra)} vezes na frase.")
print(f"A primeira letra '{letra}' aparece na posição {frase.find(letra)+1}")
print(f"A última letra '{letra}' aparece na posição {frase.rfind(letra)+1}")