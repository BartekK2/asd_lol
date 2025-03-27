
# Znajdowanie mediany
# definicja mediany: mediane definiujemy jako środkowy element ciągu posortowanego (dla nieparzystej liczby elementów)
# lub jako średnią arytmetyczną dwóch "środkowych" (dla parzystej liczby elementów)
# co prawda dla pojedynczego pobrania mediany złożoność jest identyczna (n*log(n) oczywiście)
# ale jeżeli będziemy chcieli cały czas dodawać lub usuwać elementy dalej wiedząc jaka jest nasza mediana to nie musimy już
# sortować ponownie tablicy a jedynie wstawić element w czasie log(n) co może usprawnić nam algorytm
def insert_number(num, max_heap, min_heap):
    # Dodaj do odpowiedniego kopca
    if not max_heap or num <= max_heap[0]:
        max_heap.append(num)
        reversed_max_heapify(max_heap)  # Tylko naprawianie od korzenia
    else:
        min_heap.append(-num)  # Używamy -num, by stworzyć kopiec min
        reversed_max_heapify(min_heap)  # Kopiec minimalny, więc max_heapify działa na min_heap

    # Balansowanie kopców
    if len(max_heap) > len(min_heap) + 1:
        # Przenieś największy element z max_heap do min_heap
        min_heap.append(-max_heap[0])
        max_heap[0] = max_heap[-1]
        max_heap.pop()
        reversed_max_heapify(max_heap)
        reversed_max_heapify(min_heap)
    elif len(min_heap) > len(max_heap):
        # Przenieś najmniejszy element z min_heap do max_heap
        max_heap.append(-min_heap[0])
        min_heap[0] = min_heap[-1]
        min_heap.pop()
        reversed_max_heapify(max_heap)
        reversed_max_heapify(min_heap)

def get_median(max_heap, min_heap):
    if len(max_heap) > len(min_heap):
        return max_heap[0]
    return (max_heap[0] - min_heap[0]) / 2  # Odwracamy -num w min_heap

A = [5, 15, 1, 3, 8, 7, 9, 2, 6]
max_heap = []
min_heap = []

for i in range(1,len(A)):
    print(sorted(A[0:i]))
for num in A:
    insert_number(num, max_heap, min_heap)
    print(max_heap, min_heap)
    print(f"Po dodaniu {num}, mediana: {get_median(max_heap, min_heap)}")
