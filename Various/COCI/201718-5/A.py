N = int(raw_input());
Xi = map(int, raw_input().split());
Yi = map(int, raw_input().split());

Xi.sort();
Yi.sort();

Da = True;
for i in range(len(Xi)):
    if Xi[i] > Yi[i]:
        Da = False;

if Da:
    print "DA";
else:
    print "NE";
