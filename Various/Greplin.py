#### Greplin code challenge 
#### M.A. Stankiewicz
#### 9/11/2011

S = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

def Rev(s):
    R = '';
    for c in s:
        R = c + R;
    return R

L = 1;
OK = True
while (OK):
    L += 1;
    for i in range(len(S)-L):
        sub = S[i:i+L]
        if Rev(sub) in S:
            print L, sub;
            OK = True;
            break;
    if i+L >= len(S)-1:
        OK = False


##################################

def IsP(n):
    for i in range(2,n):
        if n%i == 0:
            return False;
        if i**2 > n:
            return True;
        i += 1;

def SumFact(n):
    P = [];
    p = 2;
    while (p <= n):
        while n%p == 0:
            P.append(p);
            n /= p;
        p += 1;            
    print P,
    return sum(P)
    
F = [1,1]
for i in range(30):
    F.append( F[-1]+F[-2] )
for f in F:
    if IsP(f) and f > 227000:
        print '\nQ2:',f+1, SumFact(f+1);


##################################
        
Q3 = [3,4,9,14,15,19,28,37,47,50,54,56,59,61,70,73,78,81,92,95,97,99]
#Q3 = [1,2,3,4,6]
Cout = [0]*1200
Cout[0] = 1;

for i in Q3:
    for j in range(1100,-1,-1):
        Cout[i+j] += Cout[j];
Ans = 0;
for i in Q3:
    Ans += Cout[i]-1;
#    print i, Cout[i]
print '\nQ3:',Ans
