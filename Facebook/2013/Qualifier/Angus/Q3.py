import sys

def main():
    f1 = open('find_the_mintxt.txt', 'rU')
    f2 = open('Q3output.txt', 'w')

    for i in range(int(f1.readline())):
        line1 = [int(s) for s in (f1.readline()).split() if s.isdigit()]
        line2 = [int(s) for s in (f1.readline()).split() if s.isdigit()]
        print(i)

        m = [0]*line1[0]
        m[0] = line2[0]
        for j in range(1,line1[1]):
            m[j] = (line2[1]*m[j-1]+line2[2])%line2[3]
        
        for j in range(line1[1],line1[0]):
            m[j] = nextValue(m[j-line1[1]:j])
        
        f2.write('Case #%d: %d\n' % (i+1,m[-1]))
        
    f1.close()
    f2.close()

def nextValue(m):
    n = sorted(list(set(m)))
    compN = [-1]+n[0:-2]
        
    diff = list(map(int.__sub__, n, compN))
    del compN

    try:  
        j = next(x[0] for x in enumerate(diff) if x[1] > 1)
    except StopIteration:
        return n[-1]+1


    return n[j]-diff[j]+1

if __name__ == '__main__':
    main()
