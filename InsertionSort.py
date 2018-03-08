import sys

def InsertionSort(v):
    for i in range(1,len(v)): #o for começa do índice 1 pelo fato do que ta antes do indice 0 não ter valor para ser comparado.
        aux = v[i]
        j = i-1
        while j>=0 and aux<v[j]:
            v[j+1]= v[j]
            j = j-1
        v[j + 1] = aux

with open(sys.argv[1],'r') as arq:
   lista = arq.read().split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

print('LISTA ORIGINAL DESORDENADA:\n{}'.format(lista))
InsertionSort(lista)
print('LISTA ORDENADA:\n {}'.format(lista))