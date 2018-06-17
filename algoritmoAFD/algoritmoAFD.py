#entradas teste
#chaves: i,a/i,b/a+,a/a+,b/b+,a/b+,b
#estSegue: a+/b+/a+/b+/a+/b+
#estFinais: b+
#palavras: a/b/x/aab/babxb

chaves=input('-> ')
estSegue=input('-> ')
estFinais=input('-> ')
palavras=input('-> ')
estAtual='i'

tuplas1=tuple(chaves.split('/'))
tuplasChaves=[]

for t in range(len(tuplas1)):
    tuplas2=tuple(tuplas1[t].split(','))
    tuplasChaves.append(tuplas2)

tuplasChaves=tuple(tuplasChaves)
tuplasEstSegue=tuple(estSegue.split('/'))
tuplasEstFinais=tuple(estFinais.split('/'))
tuplasPalavras=tuple(palavras.split('/'))

for tp in range(len(tuplasPalavras)):
    for i in range(len(tuplasPalavras[tp])):
        transicao = tuplasPalavras[tp][i]
        erro = True
        for j in range(len(tuplasChaves)):
            if ((estAtual, transicao) == tuplasChaves[j]):
                estAtual = tuplasEstSegue[j]
                erro = False
                break

        if erro == True:
            print('Nao pertence')
            break

    if erro == False:
        ehFinal = False
        for k in range(len(tuplasEstFinais)):
            if estAtual==tuplasEstFinais[k]:
                print('Pertence')
                ehFinal = True
                break
        if ehFinal == False:
            print('Nao pertence')