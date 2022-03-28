# Crie um programa que tenha uma tupla com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Celular',1000,'Computador',4000,'Óculos',300,'Relógio',150,'Calculadora',50)

print('-'*45)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*45)
for pos in range(len(produtos)):
    # -------------  SOLUÇÃO GUANABARA  -------------      
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f' R$ {produtos[pos]:>10.2f}')
    # -------------  MINHA SOLUÇÃO  -------------  
    '''if ((produtos.index(produtos[pos])+1) % 2) != 0:
        #print('index impar: ',end='')
        print(f'{produtos[pos].ljust(13)}',end='.'*30)
    elif ((produtos.index(produtos[pos])+1) % 2) == 0:
        #print('index par: ',end='')
        print(f' R$ {produtos[pos]:>8.2f}')'''
print('-'*45)