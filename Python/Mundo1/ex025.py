# Crie um programa que leia o nome de uma pessoa e
# informe se ela tem silva no nome

nome = str(input('Informe o nome completo: ')).strip().upper()

print(f"Existe Silva no nome? {'SILVA' in nome}")