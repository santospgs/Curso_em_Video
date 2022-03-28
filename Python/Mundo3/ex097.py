# Faça um programa que tenha uma função chama escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
#
# Ex: escreva('Olá mundo')
#
# Saída
# ~~~~~~~~~~~~~
#   Olá mundo
# ~~~~~~~~~~~~~

def escreva(txt):
    txt = str(input('Digite uma frase: '))
    len_txt = len(txt) + 4
    print('~' * (len_txt))
    print(txt.center(len_txt))
    print('~' * (len_txt))
    
    
escreva('')