def Solve(pass1, pass2):
    # backtrack and finish
    resetcost = len(pass1)+2;
    resetstring = '*' + pass1 + '*';
    backtrackcost = 0;
    
    for i in range(min(len(pass1), len(pass2))):
        if pass1[:i+1] != pass2[:i+1]:
            # character i is bad;
            backtrackcost = (len(pass2) - i) + (len(pass1)-i) + 1;
            backtrackstring = '<'*(len(pass2)-i) + pass1[i:] + '*'

            if backtrackcost < resetcost:
                return backtrackstring;
            return resetstring;

    # one is substring of the other
    backtrackcost = abs(len(pass1)-len(pass2))+1;
    if (len(pass1) > len(pass2)):
        backtrackstring = pass1[len(pass2):] + '*';
    else:
        backtrackstring = '<'*(len(pass2)-len(pass1))+'*';

#    print len(backtrackstring), backtrackcost;
    
    if backtrackcost < resetcost:
        return backtrackstring;
    return resetstring;


N = int(raw_input());
for i in range(N):
    raw_input();
    p1 = raw_input();       p2 = raw_input();
    print Solve(p1, p2);
    
