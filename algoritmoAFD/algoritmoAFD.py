#formato entrada: estadoAtual, simboloLido, resultadoTransicao, ehFinal
entrada=input()#entrada teste: 'i,a,a+,0/i,b,b+,1/a+,a,a+,0/a+,b,b+,1/b+,a,a+,0/b+,b,b+,1'
tuplaEntrada=tuple(entrada.split('/'))
transicao={} #chave da tabela hash
for te in range(len(tuplaEntrada)):
    tuplaTe = tuple(tuplaEntrada[te].split(','))
    transicao[tuplaTe[0:2]]=tuplaTe[2:4]

estFinal=0
estAtual='i'
palavra=input()#palavra teste: 'abba'
for p in palavra:
    try:
        estFinal=transicao[estAtual,p][1]
        estAtual=transicao[estAtual,p][0]
    except KeyError:
        estFinal = 0
        break
print(estFinal)