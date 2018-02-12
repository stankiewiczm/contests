from numpy import *
#hihellolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardoesit

#   hielokatspndrm      soundfamilret
#   aeiodhklmnprst      aeioudflmnrts

ST = "hihellolookhavealookatthispalindromexxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxxsoundsfamiliardoesit"
Lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];


Pos = [];
for k in range(26):
    Pos.append([]);
for l in range(len(ST)):
    Pos[ord(ST[l])-97].append(l);


##################################################

def Search2(n1):
    count = 0;
    for a in Pos[n1]:
        for b in Pos[n1]:
            if (a < b):
                count += (b-a);
    return count;

##################################################

def Search4(n1, n2):
    count = 0;
    for a in Pos[n1]:
        for b in Pos[n2]:
            for c in Pos[n2]:
                for d in Pos[n1]:
                    if (a < b < c < d):
                        count += (c-b);
    return count;


##################################################

def Search6(n1, n2, n3):
    count = 0;
    for a in Pos[n1]:
      for b in Pos[n2]:
        if (a < b):
          for c in Pos[n3]:
            for d in Pos[n3]:
              if (b < c < d):
                for e in Pos[n2]:
                  for f in Pos[n1]:
                    if (d < e < f):
                      count += (d-c);
    return count;

##################################################

def Search8(n1, n2, n3, n4):
    count = 0;
    for a in Pos[n1]:
      for b in Pos[n2]:
        if (a < b):
          for c in Pos[n3]:
            for d in Pos[n4]:
              if (b < c < d):
                for e in Pos[n4]:
                  for f in Pos[n3]:
                    if (d < e < f):
                      for g in Pos[n2]:
                        for h in Pos[n1]:
                            if (f < g < h):
                              count += (e-d);
    return count;

##################################################

RT = 0;     Lev3 = [];      Lev4 = [];

##### 1 letter palindromes:
SUM = 112;

##### 2, 3 letter palindromes:
for A in range(26):
    SUM += Search2(A);

##### 4,5 letter palindromes:
for A in range(26):
    for B in range(26):
        SUM += Search4(A,B);

##### 6,7 letter palindromes:
for A in range(26):
    for B in range(26):
        for C in range(26):
            RT = Search6(A,B,C);
            if RT > 0:
                Lev3.append([A,B,C]);
                SUM += Search6(A,B,C);
print len(Lev3);

"""
##### 8,9 letter palindromes:
for k in Lev3:
    A = k[0];       B = k[1];       C = k[2];
    for D in range(26):
        RT = Search8(A,B,C,D);
        if RT > 0:
            Lev4.append([A,B,C,D]);
            SUM += Search8(A,B,C,D);

print len(Lev4);
"""
print SUM
