def counting_sort(A,key=lambda x: x):
    dl = len(A)
    A_2 = [0]*dl
    B = [0]*10

    for i in range(len(A)):
        B[key(A[i])] += 1

    for i in range(1,10):
        B[i] += B[i-1]


    for i in range(len(A)-1,-1,-1):
        l = key(A[i])
        pos = B[l]
        A_2[pos-1] = A[i]
        B[l] -= 1
    return A_2