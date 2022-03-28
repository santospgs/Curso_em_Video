# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá análisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

# ------ SOLUÇÃO GUANABARA ------
# Essa analisa a expressão e através de um laço, sempre que encontra um ( na expressão, adiciona-o em uma lista
# e sempre que encontra seu par ), remove o primeiro valor da lista. Dessa maneira se houve mais de um paranteses
# ou fechando ou abrindo, o comprimento da lista será diferente de zero, acusando que a expressão é inválida.
expr = str(input('Digite uma expressão'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')

# ------ MINHA SOLUÇÃO ------
'''cont_aberto = 0 # Conta a quantidade de parenteses abertos
cont_fechado = 0 # Conta a quantidade de parenteses fechados
exp = str(input('Digite uma expressão: '))
lista_exp = list(exp)

for i in range(len(lista_exp)):
    if lista_exp[i] == '(':
        cont_aberto += 1
    if lista_exp[i] == ')':
        cont_fechado += 1
        
if cont_aberto == cont_fechado:
    print('Expressão válida')
else: 
    print('Expressão inválida')'''

#solução direta com método COUNT()
'''if lista_exp.count('(') == lista_exp.count(')'):
    print('Ok, sua expressão é válida')
else:
    print('Expressão inválida')'''