DATA = [5616185650518293,  3847439647293047,  5855462940810587,  9742855507068353,
        4296849643607543,  3174248439465858,  4513559094146117,  7890971548908067,
        8157356344118483,  2615250744386899,  8690095851526254,  6375711915077050,
        6913859173121360,  6442889055042768,  2321386104303845,  2326509471271448,
        5251583379644322,  1748270476758276,  4895722652190306,  3041631117224635,
        1841236454324589,  2659862637316867] ;
Ss = [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2];


DIG = [];
for i in range(len(DATA)):
    DIG.append([]);
    n = DATA[i];
    while n > 0:
        DIG[i].append(n%10);
        n /= 10;

def HitCount(num, digs):
    hits = 0;
    for i in range(len(digs)):
        if (num%10) == digs[i]:
            hits += 1;
        num /= 10;
    return hits;


def Check(index):
    for e in ANS[index]:
        print e
        Ok = True;
        for n in range(len(DATA)):
            if HitCount(e, DIG[n][0:index+1]) > Ss[n]:
                Ok = False;
        if not Ok:
            ANS[index].remove(e);
    return 
            



#ANS = [ [0,1,2,3,4,5,6,7,8,9] ];
ANS = [ [0] ];

for j in range(1,16):
    ANS.append([]);
    next = 10**(j-1);
    for d in range(10):
        for e in ANS[j-1]:
            Ok = True;
            test = e+next*d;
            for q in range(len(DIG)):
                if HitCount(test, DIG[q][0:j]) > Ss[q]:
                    Ok = False;
            if Ok:
                ANS[j].append( e+next*d );
    print j, len(ANS[j])#, ANS[j]


