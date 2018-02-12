from Numeric import *

# Have following: 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p;

denoms = [1, 2, 5, 10, 20, 50, 100, 200]

nums = 0

def solve(amount, denom=denoms, vals=[]):
    global nums
    
    if amount == 0:
        nums += 1
        return
    if not denom: return
    d = denom[0]
    for i in range(0, amount / d + 1):
        #print d, i
        solve(amount - i * d, denom[1:], vals + [i])
    
