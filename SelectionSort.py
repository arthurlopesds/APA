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

with open('num.1000.1.in','r') as arq:
    lista = arq.read().split()

for i in range (0,len(lista)):
    lista[i] = int(lista[i])

SelectionSort(lista)
print(lista)