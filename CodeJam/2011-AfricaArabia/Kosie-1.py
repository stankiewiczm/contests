C=int(raw_input())

for c in xrange(1, C+1):
    n=int(raw_input())
    segments = raw_input().split()
    red=[]
    blue=[]
    for s in segments:
        if s[-1]=='R':
            red.append(int(s[:-1]))
        else:
            blue.append(int(s[:-1]))
    red.sort()
    blue.sort()
    l = min(len(red), len(blue))
    print "Case #%d: %d"%(c, sum(red[len(red)-l:])+sum(blue[len(blue)-l:])-l*2)
