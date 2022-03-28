#?
#? Faça um programa que tenha uma função notas() que pode receber várias notas
#? de alunos e vai retornar um dicionário com as seguintes informações:
#? - quantidade de notas
#? - a maior nota
#? - a menor nota
#? - a média da turma
#? - a situação (ruim/razoavel/boa)
#? adicione também as docstrings da função


def notas(*nota,sit=False):
    """
    --> Função para analisat notas e situação de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: (opcional) Indica se a situação será exibida ou não.
    :return: Dicionário com várias informações sobre a situação da sala.
    """

    notasDic = dict()

    s = 0
    for n in nota:
        s += n 

    maior = menor = n
    for n in nota:        
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    notasDic['total'] = len(nota)
    notasDic['maior'] = maior
    notasDic['menor'] = menor    
    notasDic['media'] = s / len(nota)

    if sit:
        if (notasDic['media'] < 5):
            notasDic['situacao'] = 'ruim'
        elif (5 >= notasDic['media'] < 7):
            notasDic['situacao'] = 'razoável'
        else:
            notasDic['situacao'] = 'boa'

    return notasDic       
    
print(notas(7,4,4,1,sit=True))
