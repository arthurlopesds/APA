import sys

def SelectionSort(v):
    for i in range(0,len(v)-1):
        menor=i
        for j in range(i+1,len(v)):
            if v[menor]>v[j]:
                menor=j
        if i!= menor:
            aux=v[i]
            v[i]=v[menor]
            v[menor]=aux

with open(sys.argv[1],'r') as arq:
    lista = arq.read().split()

for i in range (0,len(lista)):
    lista[i] = int(lista[i])

print('LISTA ORIGINAL DESORDENADA:\n{}'.format(lista))
SelectionSort(lista)
print('LISTA ORDENADA:\n {}'.format(lista))