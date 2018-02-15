def Query(h):
    r = 0.;
    for i in range(N-1):
        x0 = i;         x1 = i+1;
        y0 = H[i];      y1 = H[i+1];
        if (y0 <= h) and (y1 <= h):
            r += 2*h-(y0+y1);

        else:
            if (y0 > h) and (y1 < h):
                xint = (h-y0)/float(y1-y0);
                r += (1-xint) * (h-y1);
            if (y0 < h) and (y1 > h): 
                xint = (h-y0)/float(y1-y0);
                r += xint * (h-y0);
                
#        print h, (x0,y0), (x1,y1), r
        
    print "%3.3f" % (r/2.)

[N, M] = map(int, raw_input().split() );
H = map(int, raw_input().split() );
for case in range(M):
    inp = raw_input().split();
    if inp[0] == 'Q':
        Query(int(inp[1]));
    else:
        H[int(inp[1])] = int(inp[2]);
    
