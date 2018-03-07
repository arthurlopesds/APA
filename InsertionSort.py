def InsertionSort(v):
    for i in range(1,len(v)):
        aux = v[i]
        j = i-1
        while j>=0 and aux<v[j]:
            v[j+1]= v[j]
            j = j-1


        v[j + 1] = aux


with open('couting.txt','r') as arq:
    lista = arq.read().split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

InsertionSort(lista)
print(lista)