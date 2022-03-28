# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com a palavra santo.

nome_cidade = str(input('Insira o nome da cidade:')).strip().lower()

print(f"Existe Santo no nome da cidade? {'santo' in nome_cidade}")
print(f"Existe Santo no nome da cidade? {nome_cidade[:5].upper() == 'SANTO' }")