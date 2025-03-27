def parent(ind):
    return (ind-1)//2
def left(ind):
    return ind*2+1
def right(ind):
    return ind*2+2


def max_heapify(A,ind,size=None): # złożoność log(n) gdzie n to ilość elementów poddrzewa od indeksu uruchomionego 
    largest = ind
    l = left(ind)
    r = right(ind)
    if size is None:
        size = len(A)
    if l < size and A[l] > A[largest]:
        largest = l
    if r < size and A[r] > A[largest]:
        largest = r
    if largest != ind:
        A[ind], A[largest] = A[largest], A[ind]
        max_heapify(A,largest,size) # ta rekurencja w sumie może być niepotrzebna, zwalnia algorytm (na kolokwium użyj bez)

def reversed_max_heapify(A,size=None): # taki heapify tylko że od dołu, przydatny gdy dodajemy elementy na koniec listy
    if size is None:
        size = len(A)
    ind = size-1
    while ind != 0:
        if A[parent(ind)] < A[ind]:
            A[parent(ind)], A[ind] = A[ind], A[parent(ind)]
        ind = parent(ind) # przykład pozbycia się rekurencji na rzecz algorytmu iteracyjnego


# ważne!!! to uruchamiamy tylko po to żeby dany węzeł przerzucić w dół, czyli naszymi założeniami są to że 
# lewe i prawe poddrzewo jest już kopcem min/max (w tym przypadku ofc. max)
# nie możemy tego uruchomić bez spełnienia tych założeń - otrzymamy jakieś pierdoły

# Przekształcenie dowolnej tablicy w kopiec typu max:

def build_max_heap(A): # złożoność O(n)
    l = len(A)
    for i in range(l//2-1,-1,-1): # to jest tylko optymalizacja, pomijamy liście dzięki metodzie liczenia l//2-1  
        max_heapify(A,i,l)

A = [4,1,3,2,16,9,10,14,8,7]
build_max_heap(A)

# build_max_heap działa na takiej zasadzie że pomija liście - jako iż one są już kopcami typu max
# a następnie dla ich rodziców uruchamia max_heapify() co sprawi że rodzic będzie większy niż syn itd...

# sortowanie heap sort

def heap_sort_dep(A): # zakładamy że A jest kopcem max złożoność n*log(n) (ponieważ dla każdego elementu uruchamiamy heapify?)
    l = len(A)
    while l > 1:
        A[l-1], A[0] = A[0], A[l-1]
        max_heapify(A,0,l-1)
        l -= 1


# okej teraz złączmy w całość to co zrobiliśmy żeby stworzyć pełne sortowanie kopcowe nie myśląc o tym czy podana
# tablica na początku była kopcem tudzież nie

def heap_sort(A):
    build_max_heap(A) # czyli najpierw sprawiamy że tablica jest kopcem max
    heap_sort_dep(A) # następnie używamy funkcji zależnej od poprzedniej własności

heap_sort(A)