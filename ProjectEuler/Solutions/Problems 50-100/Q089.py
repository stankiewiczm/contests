RM = [0,0,100,500,0,0,0,0,1,0,0,50,1000,0,0,0,0,0,0,0,0,5,0,10,0,0];
F = open('../TXTdata/roman.txt','r');       
B = [0,1,2,3,2,1,2,3,4,2];
Ans = 0;

def Optimize(S):
    Sym = [];    
    for c in S:
        Sym.append( RM[ord(c)-65] );
    Val = Sym[0];
    for k in range(1,len(Sym)):
        Val += Sym[k];
        if Sym[k-1] < Sym[k]:
            Val -= 2*Sym[k-1];

    Best = Val/1000 + B[(Val/100)%10] + B[(Val/10)%10] + B[Val%10];
    return len(S)-Best;

    
for i in range(1000):
    S = F.readline().split()[0];
    Ans += Optimize(S);
print Ans
