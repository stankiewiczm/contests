def C(n,r):             # Choose function
    R = 1;
    for i in range(r):
        R = (R*(n-i))/(i+1);
    return R;

def Solve(nProblems, nOptions):
    pRight = 1./(nOptions);
    pWrong = 1 - pRight;
    cumulative = 0.;
    probability = 0.;
    
    for nRight in range(nProblems+1):
        nWrong = nProblems - nRight;

        prob = C(nProblems, nRight) * pRight**nRight * pWrong**nWrong;
        score = 100. * nRight / nProblems;

        probability += prob;
        cumulative += prob*score;
        
        print "%5.1f %0.8f" % (score, prob);

    print "Total probability %1.7f" % (probability);
    print "Expected score %1.7f" % (cumulative);

