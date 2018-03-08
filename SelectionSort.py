import sys

def SelectionSort(v):
    for i in range(0,len(v)-1): # limite é até um valor antes do valor final,pois o valor final ja vai estar ordenado
        menor=i #menor recebe o indice do primeiro numero
        for j in range(i+1,len(v)): #começa o 2º numero e vai até o ultimo, nao começa do primeiro, pois o primeiro ja vai
                                    #ser o comparado
            if v[menor]>v[j]: '''comparando se o valor do numero menor é maior do que os outros que estão na lista
                                se for, menor recebe o indice do valor que é o menor'''
            menor=j
        if i!= menor: #se o valor for diferente do primeiro valor que estava na variavel menor no começo
                    #ocorre a troca de posições dos valores
            aux=v[i]
            v[i]=v[menor]
            v[menor]=aux

with open(sys.argv[1],'r') as arq:
    lista = arq.read().split()

for i in range (0,len(lista)):
    lista[i] = int(lista[i])

print('LISTA ORIGINAL DESORDENADA:\n{}'.format(lista))
print('\n\n\n')
SelectionSort(lista)
print('LISTA ORDENADA:\n {}'.format(lista))