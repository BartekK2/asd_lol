# Znajdowanie n-tego największego/najmniejszego elementu w tablicy

# tworzymy kopiec minimalny/maksymalny o rozmiarze k (gdzie k oznacza k-ty największy/najmniejszy element)

A = list(range(100))
k = 5
B = A[0:k]
build_max_heap(B)
for i in range(k,len(A)):
    if A[i] < B[0]:
        B[0] = A[i]
        max_heapify(B,0,k)
print(f"{k}-ty najmniejszy element w tablicy A to {B[0]}")