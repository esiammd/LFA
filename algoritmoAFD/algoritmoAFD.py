#entradas teste
#chaves: i,a/i,b/a+,a/a+,b/b+,a/b+,b
#estSegue: a+/b+/a+/b+/a+/b+
#estFinais: b+
#palavras: a/b/x/aab/babxb

chaves=input('Informe as chaves "estadoAtual + transição" no seguinte formato: estado1, transição1/estado2, transição2-> ')
estSegue=input('Informe respectivamente os estados gerados pela opeção descrita acima no formato: estado1/estado2-> ')
estFinais=input('Informe os estados finais no formato: estado1/estado2-> ')
palavras=input('Informe as palavras que deseja verificar se pertence a linguagem no fomrato: palavra1/palavra2-> ')
estAtual='i'

tuplas1=tuple(chaves.split('/'))
tuplasChaves=[]
t=0
while t<len(tuplas1):
    tuplas2=tuple(tuplas1[t].split(','))
    tuplasChaves.append(tuplas2)
    t+=1

tuplasChaves=tuple(tuplasChaves)
tuplasEstSegue=tuple(estSegue.split('/'))
tuplasEstFinais=tuple(estFinais.split('/'))
tuplasPalavras=tuple(palavras.split('/'))

tp=0
while tp<len(tuplasPalavras):
    i = 0
    while i < len(tuplasPalavras[tp]):
        transicao = tuplasPalavras[tp][i]
        erro = True
        j = 0
        while j < len(tuplasChaves):
            if ((estAtual, transicao) == tuplasChaves[j]):
                estAtual = tuplasEstSegue[j]
                erro = False
                break
            j += 1

        if erro == True:
            print('A palavra "{}" não pertence a linguagem'.format(tuplasPalavras[tp]))
            break
        i += 1

    if erro == False:
        ehFinal = False
        k = 0
        while k < len(tuplasEstFinais):
            if estAtual==tuplasEstFinais[k]:
                print('A palavra "{}" pertence a linguagem'.format(tuplasPalavras[tp]))
                ehFinal = True
                break
            k += 1
        if ehFinal == False:
            print('A palavra "{}" não pertence a linguagem'.format(tuplasPalavras[tp]))
    tp+=1