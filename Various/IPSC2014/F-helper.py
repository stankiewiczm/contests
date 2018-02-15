Fpi = open('pi1000000.txt','r');

for line in Fpi:
    Digits = line[2:-1];


count = [0]*10;
count[0] = 1;
for i in range(9):
    count[int(Digits[i])] += 1;
for i in range(9,len(Digits)):
    count[int(Digits[i])] += 1;
    count[int(Digits[i-9])] -= 1;
    if min(count) == 1:
        print i-7, Digits[i-8:i+1]
