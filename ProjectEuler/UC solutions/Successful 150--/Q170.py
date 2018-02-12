from Numeric import *

# This code checks for 2-digit value of n.  The single digit values of n maxed out at 9786105234 = 9*(1087345 + 26)

F = [1,1,2,6,24,120,720,5040,40320,362880, 3628800];        LIST= [0];
LEN = 10;

def FiddleCheck2(lst, MAX):
    Np = 10*lst[0]+lst[1];#        ls1 = int(9.9/(Np+0.01));
    if (lst[0] == 0) or (lst[2] == 0):# or (Np >= 30):
        return 0;
    if (Np*lst[2] > 100) or (Np*(10*lst[2]+lst[3]) < 960):
        return 0;
    
    for a in arange(3,LEN):
        if (lst[a] != 0):
            N1 = 0;     N2 = 0;
            for c in range(2,a):
                N1 = N1*10+lst[c];
            for c in range(a,LEN):
                N2 = N2*10+lst[c];


#            print lst, Np, N1, N2;
            
            chck = zeros(10);
            P = N1*Np;
            while (P != 0):
                chck[P%10]+= 1;
                P /= 10;
            P = N2*Np;
            while (P != 0):
                chck[P%10]+= 1;
                P /= 10;
#
#            chck[0] += 1;
#
            if (max(chck) == min(chck)):
                lg = int(log10(Np*N2))+1;
                if (Np*(N1*10**lg+N2) >= max(LIST)):
                    print Np,'*', N1, N2, '->', Np*N1, Np*N2, '   ', Np*(N1*10**lg+N2)

                LIST.append( (N1*10**lg+N2)*Np );
                
#               return (N1*10**lg+N2)*Np;
    return 0;



def lexpermute(l,start):
	global total
	total+=1
	if(total % 100000  == 0):
            print total, l
#	if l[0] == 2:
        FiddleCheck2(l, 0);

	if(start<len(l)):
		for i in range(len(l)-2,start-1,-1):
			for j in range(i+1,len(l)):
				l[i],l[j]=l[j],l[i]
				lexpermute(l,i+1)
			temp=l[i]
			l.remove(l[i])
			l.append(temp)
 
total=0
l=range(0,10)
lexpermute(l,0)
