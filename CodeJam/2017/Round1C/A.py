from math import pi

def Solve(k, stack):
    Area = [];
    for pair in stack:
        Area.append(2*pair[0]*pair[1]);

    results = [];
    for starti in range(len(stack)-k+1):
        topView = stack[starti][0]**2;
        sideView = Area[starti];

        remainder = Area[starti+1:]
        remainder.sort();
        remainder.reverse();
        sideView += sum(remainder[:k-1])

        results.append(topView + sideView);
    return max(results)*pi

T = int(raw_input());
for q in range(T):
    [N, K] = map(int, raw_input().split());

    pancakes = [];
    for i in range(N):
        pancakes.append( map(int, raw_input().split()) )

    pancakes.sort();
    pancakes.reverse();
    
    print "Case #%d:" % (q+1),
#    print K, pancakes
    print "%.9f" % Solve(K, pancakes);

