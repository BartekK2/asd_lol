def radix_sort(A):
    # pos w sensie od tyłu, dla pos=0 cyfra jedności, pos=1 cyfra dziesiątek
    def digit(liczba,pos=0):
        return liczba % (10**(pos+1)) // 10**pos
    i = 1
    longest_digit = max(A)
    while longest_digit // 10 != 0:
        longest_digit = longest_digit // 10
        i += 1
    for j in range(i):
        A = counting_sort(A,key=lambda x: digit(x,pos=j))
    return A