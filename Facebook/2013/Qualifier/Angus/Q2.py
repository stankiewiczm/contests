import sys
import re

def main():
    f1 = open('balanced_smileystxt.txt', 'rU')
    f2 = open('Q2output.txt', 'w')

    cnt = 0
    for line in f1:
        if cnt > 0:

            cleanString = clean(line)
            len1 = len(cleanString)
            if len1 > 0:
                while True:
                    cleanString = clean(cleanString)
                    len2 = len(cleanString)

                    if len1-len2 == 0:
                        break
                    else:
                        len1 = len2

            if len(cleanString) > 0:
                f2.write('Case #%d: NO\n' % cnt)
            else:
                f2.write('Case #%d: YES\n' % cnt)
            
        cnt = cnt+1
        
    f1.close()
    f2.close()

def clean(inString):
    # lower case and remove trailing end of line character
    outString = (inString.lower()).strip('\n\r')
    # remove all unimportant characters
    outString = re.sub(re.compile('[^:^)^(]+'), ' ', outString)
    # remove expressions of the form (:*n)
    outString = remSpecial(outString)
    # remove any smileys
    outString = remSmiley(outString)
    # remove trivially bracketed expressions
    outString = remTrivial(outString)
    # remove floating colons
    remColon(outString)
    # remove remaining colons
    outString = re.sub(r':', ' ', outString)
    # remove trivially bracketed expressions
    outString = remTrivial(outString)
        
    outString = outString.replace(" ", "")

    return outString

def remSmiley(inString):
    outString = re.sub(r':\)', ' ', inString)
    outString = re.sub(r':\(', ' ', outString)

    return outString

def remTrivial(inString):
    outString = re.sub(re.compile('\(\)'), ' ', inString)
    outString = re.sub(re.compile('\([ ]+\)'), ' ', outString)

    return outString

def remSpecial(inString):
    return re.sub(re.compile('\([ :]+\)'), ' ', inString)

def remColon(inString):
    # must come after removing smileys
    outString = re.sub(re.compile('[ ]+[:]+[ ]+'), ' ', inString)
    outString = re.sub(re.compile('[ ]+[:]+'), ' ', outString)
    outString = re.sub(re.compile('[:]+[ ]+'), ' ', outString)

    return outString

if __name__ == '__main__':
    main()
