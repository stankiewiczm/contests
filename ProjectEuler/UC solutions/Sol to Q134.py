# if you have 99 and want 98 mod 100, get_m(99,98,2) will return 2, 
# since 99*2 = 98 mod 100
def get_m(base, wanted, pow10): # base,wanted < 10**pow10 ; pow10 > 0
    if pow10 == 1: return [x for x in xrange(10) if x*base % 10 == wanted]
    p10m = 10**(pow10-1)
    halfsol = get_m(base % p10m, wanted % p10m, pow10-1)
    return [x*p10m + y for y in halfsol for x in xrange(10)
            if (x*p10m + y)*base % (10**pow10) == wanted]
 
def inner(p1, p2):
    # want a power 10 modulus of same length as p1
    pow10 = len(str(p1))
    # determine possibilities for last pow10 digits of a p2 multiplier
    last_digits = get_m(p2 % 10**pow10, p1 % 10**pow10, pow10)
    # now go and stick numbers in front of those sets of digits until we 
    # get an ending of p1 when multiplied by p2
    i,sols = -1, []
    for ld in last_digits:
        while 1:
            i += 1
            real_i = (i * 10**pow10 + ld)*p2
            if real_i % 10**pow10 == p1:
                sols.append(real_i)
                break
    # pick smallest solution
    return min(sols)
 
LIMIT = 10**6
total,p1 = 0,0
for p2 in prime_list()[2:]:
    if p1 > LIMIT: break
    total += inner(p1,p2)
    p1 = p2
print total