from numpy import *

File = open('../TXTdata/base_exp.txt','r');
Log = [];
for n in range(1000):
    S = File.readline();
    for k in range(len(S)):
        if S[k] == ',':
            a = int(S[0:k]);
            b = int(S[k+1:len(S)]);
            Log.append(b*log10(a));
print Log.index(max(Log))+1
