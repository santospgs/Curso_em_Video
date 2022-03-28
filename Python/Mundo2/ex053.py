# crie um programa que leia uma frase e diga se ela é um palindromo
#RESOLUÇÃO DO CURSO
'''
frase = str(input('Digite uma frase)).strip().upper() #ENTRADA FRASE COM STRIP() PRA REMOVER OS ESPAÇO DO COMEÇO E FIM E UPPER() PRA DEIXAR MAIUSCULO
palavras = frase.split #SPLI() PARA SEPARAR A FRASE EM PALAVRAS INDIVIDUAIS EM UMA LISTA
junto = ''.join(palavras) #.JOIN() PARA JUNTAR TODAS AS PALAVRAS SEM NENHUM ESPAÇO
inverso = ''

for letra in range(len(junto) - 1, -1, -1) #LEN() PEGA O TAMANHO TOTAL DA PALAVRA, OU SEJA, A POSIÇÃO DA ULTIMA LETRA, E COM O -1 LE ELA DE TRÁS PRA FRENTE 
    inverso += junto[letra] #O INVERSO VAI SER O INVERSO + AS LETRAS TODAS JUNTAS
print(junto,inverso)

'''


frase = str(input('Informe a frase: ')).upper()

frase_limpa = frase.replace(' ','')
frase_invertida = frase_limpa[::-1]

#print(frase_invertida)
#print(frase_invertida)

print(f'A frase {frase}')
if frase_invertida == frase_limpa:
    
    print('é um palindromo')
else:
    print('náo é um palindromo')
