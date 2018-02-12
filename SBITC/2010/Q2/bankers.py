

def profit(M_list,D_list,n,t):       
    #M_list=[1000,1000,1000,1000,120]
    #D_list=[0,100,-50,150,50]
    #N=[5]
    #profits=[]
    #n=N
    P_list=[0]*n
    #D_list=D[t]
    #M_list=M[t]
    P_list[-1]=M_list[-1]
    for i in range(n-2,-1,-1):
        P_list[i]=min(P_list[i+1]-D_list[i+1],M_list[i])
    profits = sum(P_list)
    #for n in N:
    print "Case #"+str(t)+": "+str(profits)


T=int(raw_input())
for t in range(0,T,1):
    N = int(raw_input())
    M=[int(raw_input())]
    D=[0]
    for n in range(1,N,1):
        line = raw_input()
        Mthis,Dthis=line.split(' ')
        M.append(int(Mthis))
        D.append(int(Dthis))
#    print t, D, M
    profit(M,D,N,t+1)
#    print M


##N=[]
##data=[]
##M=[]
##D=[]
##for t in range(0,T,1):
##    N.append(int(raw_input()))
##    data.append([])
##    Mthis=[(data[t].append(int(raw_input())))]
##    Dthis=[0]
##    for n in range(1,N[-1],1):
##        data[t].append(str(raw_input()))
##        M1,D1=data[t][n].split(' ')
##        Mthis.append(int(M1))
##        Dthis.append(int(D1))
##    M.append(Mthis)
##    D.append(Dthis)

        
