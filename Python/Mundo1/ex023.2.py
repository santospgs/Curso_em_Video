
while True:
    valor = int(input('Valor sacado: '))
    index = 0
    notas = [50,20,10,1]
    snd = ['U: ','D: ','C: ','M: ','DM: ']
    tam_valor = len(str(valor))
    v = 1

    for i in range(0, tam_valor):
        if tam_valor > len(snd):
            print('Valor excede o limite!')
            break
        else:
            n = valor // v % 10
            print(snd[i],n)
            v *= 10
        

        

    
   


    
