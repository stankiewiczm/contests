from numpy import *

s = "znkupuq zgql ku wgi bqi nvq ufsqixbtnf cszuwu tc cbtrr pvrfuqghru bn gbbgsac dqnw gbzufg xgqbtstxgfbc"

Words = s.split();

ALPH = [];
for i in range(26):
    ALPH.append( chr(i+97) );

def Check(lst, n):
    R = False;
    for l in lst:
        if chr(l+97) in n:
            R = True;
    return R


def Show(lst):
    for l in lst:
        print chr(l+97),
    print " "
"""
    
for a in range(26):
    for b in range(a):
        for c in range(b):
            for d in range(c):
                for e in range(d):
                    
                    Good = True;
                    for w in Words:
                        if Check([a,b,c,d,e],w) == False:
                            Good = False;
                    if (Good):
                        Show([e,d,c,b,a]);
#                        print e,d,c,b,a
"""
freq = zeros(26,int);
for c in s:
    if c != ' ':
        freq[ord(c)-97] += 1;
#        print chr(96+(ord(c)-97)),
#    else:
#        print ' '

print freq
print "[a b c d e f g h i j k l m n o p q r s t u v w x y z]"

print 'bgqu'
print 'cbtrr'

#gbbb sac

#atta...
#anna...
#assa...
#esse...
#ette...

# e it san

#ku tc bn wgi bqi nvq 

#vowels: u, t/c, b/n, g(w/i)

#vowels: q, u,

s = "znkupuq zgql ku wgi bqi nvq ufsqixbtnf cszuwu tc cbtrr pvrfuqghru bn gbbgsac dqnw gbzufg xgqbtstxgfbc"
#                  so why try 

Code = [];
for i in range(26):
    Code.append('.');
#Code[17] = 'l'          # R = l,o       (e/s)
#Code[19] = 'a'

#Code[6] = 'a';
#Code[1] = 't';
#Code[18] = 'l';
#Code[0] = 'e'
#Code[2] = 's'


#Code[10] = 'a';
#Code[20] = 'm';
#Code[22] = 'w';
#Code[6]  = 'h';
#Code[8]  = 'y';
#Code[1]  = 't';
#Code[16] = 'r';

Code = ['k', 't', 's', 'f', '.', 'n',
        'a', 'b', 'y', '.', 'w', 'd',
        '.', 'o', '.', 'v', 'r', 'l',
        'c', 'i', 'e', 'u', 'm', 'p', '.', 'h'];
#Code[1] = 't';
#Code[13] = 'o';
#Code[6] = 'a';
#Code[25] = 'h';
#Code[20] = 'e';
#Code[5] = 'n';
#Code[2] = 's';
#Code[10] = 'w';
#Code[15] = 'v'
#Code[16] = 'r'
#Code[11] = 'd';

# e it san

print s;        s2 = '';
for i in range(len(s)):
    if s[i] != ' ':
        s2 = s2 + Code[ord(s[i])-97];
        #New = New + Code(ord(c)-97);
    else:
        s2 += ' ';
print s;
print s2;

# Two letter words
# am, an, as, at
# be, by, do, go, he, hi, if, in, is, it, 
# me, of, on, or, ox, to, up, us, we



# IF "bn" == "to", must have "g" = a

