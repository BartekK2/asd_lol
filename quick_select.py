def quick_select(A,p,r,k):
    if p==r:
        return A[p]
    
    pivot = partition(A,p,r)
    if pivot == k:
        return A[pivot]
    if pivot < k:
        return quick_select(A,pivot+1,r,k)
    else:
        return quick_select(A,p,pivot-1,k)
