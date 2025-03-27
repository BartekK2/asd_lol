from math import inf, floor
from random import randint

inv = 0
# funkcja która z dwóch podtablic tablicy scala je w jedną, w taki sposób by utworzona tablica była posortowana
def merge(A,p,q,r):
    global inv
    n1 = q-p+1
    n2 = r-q
    # dla przykładu gdy chce wywołać merge na A=[1,2,3,4,5...,20] używając p=3 q=6 r=10
    # to n1=4, n2=4 ponieważ lewa i prawa podtablica zawiera 4 elementy (L=[3,4,5,6], R=[7,8,9,10])
    L = [0]*n1 + [inf]# (n1+1) ponieważ chcemy zachować miejsce dla infinity
    R = [0]*n2 + [inf]
    # kopiujemy
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+j+1]

    # indeksy idące po podtablicach
    i=0
    j=0
    # idziemy po indeksach tablicy początkowej (A) i ustawiamy je w zależności od tego jakie są w L i R (które mniejsze)
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            inv += (q-i+1) # LICZENIE INWERSJI
            A[k]=R[j]
            j+=1
    
def mergeSort(A,p,r):
    # no i lecąc tak dalej mamy wszystko gotowe bo ostatecznie skończymy z podtablicami 1 elementowymi i cacy sie poukłada
    if p < r:
        q = floor((p+r)/2)
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

mergeSort(A,0,len(A)-1)