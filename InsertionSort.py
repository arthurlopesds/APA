import sys

def InsertionSort(v):
    for i in range(1,len(v)): #o for começa do índice 1 pelo fato do que ta antes do indice 0 não ter valor para ser comparado.
        aux = v[i] #auxiliar recebe o valor atual
        j = i-1 #j é decrementado para ficar com o valor anterior ao atual para fazer a comparação
        while j>=0 and aux<v[j]: #o laço vai rodar enquanto o não chegar no primeiro valor da lista e enquanto o valor
                                #atual for menor do que o anterior
            v[j+1]= v[j]        #acontece a troca
            j = j-1             #decrementa o valor de j para ir voltando na lista
        v[j + 1] = aux          #o valor é colocado no seu devido lugar

with open(sys.argv[1],'r') as arq: #abrindo arquivo para leitura
   lista = arq.read().split()  #lendo arquivo e quebrando num array e armazenando na variavel lista

for i in range(len(lista)):
    lista[i] = int(lista[i]) #conversao para int

print('LISTA ORIGINAL DESORDENADA:\n{}'.format(lista))
print('\n\n\n')
InsertionSort(lista) #chamada da função
print('LISTA ORDENADA:\n {}'.format(lista))