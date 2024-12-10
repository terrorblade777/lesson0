numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for urban in  numbers:
    a_ = 1
    if urban > 1:
        for i in range(2, int(urban ** 0.5) + 1):
            if urban % i == 0:
             a_= 0
             break

    if urban > 1:
        if a_:
            primes.append(urban)
        else:
            not_primes.append(urban)
        # for urban in enumerate(primes):
        #         print(primes)
print (primes)
print (not_primes)





