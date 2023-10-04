def largest_power(N):
    k = 0
    while 3 ** k < N:
        k += 1
    return k - 1 if k > 0 else -1
