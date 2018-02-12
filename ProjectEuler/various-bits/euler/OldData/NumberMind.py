from Numeric import *


DATA = [5616185650518293, 3847439647293047, 5855462940810587, 9742855507068353,
        4296849643607543, 3174248439465858, 4513559094146117, 7890971548908067,
        8157356344118483, 2615250744386899, 8690095851526254, 6375711915077050,
        6913859173121360, 6442889055042768, 2321386104303845, 2326509471271448,
        5251583379644322, 1748270476758276, 4895722652190306, 3041631117224635,
        1841236454324589, 2659862637316867];

RIGHT = [2, 1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2];

LEN = 22;

#DATA =  [90342, 70794, 39458, 34109, 51545, 12531];
#RIGHT = [2,0,2,1,2,1];

def Check(CurrData, CurrRight, Dig):
    for i in arange(len(CurrData)):
        if (CurrRight[i] == 0):
            if (CurrData[i]%10 == Dig):
                return False;
    return True;



def Recurse(tData, tRight, LIST):
    if (tData[0] <= 1e12):
        if sum(tRight) == 0:
            print LIST;
#$        else:
#            print "Balls"
        return  ;
#        print tData, tRight, LIST;
#        return ;
        
#    if len(LIST) >= 16:
#        print LIST;
#        return;

    for a in arange(10):            # Digit to add to string
        tmpData = [];
        tmpRight = zeros(LEN);       
        for b in arange(len(tData)):        # Counter
            tmpData.append(tData[b]/10);
#            print b, len(tData)
            if (tData[b]%10 == a):
                tmpRight[b] = tRight[b]-1;
            else:
                tmpRight[b] = tRight[b];

        nList = [];
        for i in LIST:
            nList.append(i);
        nList.append(a);

        if (min(tmpRight) >= 0):
            if len(nList) == 3:
                print nList
            Recurse(tmpData, tmpRight, nList)

#        else:
#            print tmpRight

#        for c in arange(LEN):
#            print tmpData[c], tmpRight[c]
                
                
#    for a in arange(10):
#        if Check(


    return True;


Recurse(DATA, RIGHT,[]);
print "Done"
