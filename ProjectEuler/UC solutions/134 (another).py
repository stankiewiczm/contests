def find_div(p1, p2):
    # Find a multiple of p2 that ends with the
    # digits of p1.
    # Does long division backwards to do so
 
    length = len(str(p1))
    length_mask = 10 ** length
 
    multiplier = 10
    n = 0
 
    # really, this 'for' simply prevents an infinate loop
    for a in range(length):
        for n in range(n, multiplier, multiplier / 10):
            if (p2 * n) % multiplier == p1 % multiplier:
                if (p2 * n) % length_mask == p1:
                    return p2 * n
                break
        multiplier *= 10
 
total = 0
 
p1 = primes[2]
for p2 in primes[3:]:
    total += find_div(p1, p2)
    p1 = p2
 
print total
