import sys
import collections

def main():
    f1 = open('beautiful_stringstxt.txt', 'rU')
    f2 = open('Q1output.txt', 'w')

    cnt = 0
    for line in f1:
        if cnt > 0:
            tot = 0;
            cleanString = clean(line)

            alphabet = collections.defaultdict(int)
            for c in cleanString:
                alphabet[c] += 1

            counter = 0
            for c in sorted(alphabet, key=alphabet.get, reverse=True):
                if c.isalpha():
                    tot = tot + alphabet[c]*(26-counter)
                    counter = counter + 1
                
            f2.write('Case #%d: %d\n' % (cnt,tot))
            
        cnt = cnt+1
        
    f1.close()
    f2.close()

def clean(instring):
    outstring = ((instring.lower()).replace(" ", "")).strip('\n\r')

    return outstring

if __name__ == '__main__':
    main()
