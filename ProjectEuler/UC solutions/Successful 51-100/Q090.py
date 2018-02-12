from Numeric import *;

SLIST = list();

def MakeSeqs():
    for i in arange(1024):
        I = i;
        Seq = zeros(10);
        for j in arange(10):
            Seq[j] = I%2;
            I = I/2;
        if sum(Seq) == 6:
            New = list();
            for k in arange(10):
                if (Seq[k] == 1):
                    New.append(k);
            SLIST.append(sort(New));


def Check(list1, list2):
    MDig = zeros(100);

    for a in arange(len(list1)):
        for b in arange(len(list2)):
            MDig[10*list1[a]+list2[b]] = 1;
            MDig[10*list2[a]+list1[b]] = 1;

    if (9 in list2):
        for a in arange(len(list1)):
            MDig[10*list1[a]+6] = 1;
            MDig[60+list1[a]]   = 1;
    if (6 in list2):
        for a in arange(len(list1)):
            MDig[10*list1[a]+9] = 1;
            MDig[90+list1[a]]   = 1;

    if (9 in list1):
        for a in arange(len(list2)):
            MDig[10*list2[a]+6] = 1;
            MDig[60+list2[a]]   = 1;
    if (6 in list1):
        for a in arange(len(list2)):
            MDig[10*list2[a]+9] = 1;
            MDig[90+list2[a]]   = 1;


    if (MDig[1] == 1) and (MDig[4] == 1) and (MDig[25] == 1) and (MDig[81] == 1):
        if (MDig[9] == 1) and (MDig[16] == 1) and (MDig[36] == 1):
            if (MDig[49] == 1) and (MDig[64] == 1):

                return 1;
    return 0;
        


TOT = 0;
MakeSeqs();
for L1 in arange(210):
    for L2 in arange(L1):
        TOT += Check(SLIST[L1],SLIST[L2]);

print "All done", TOT
