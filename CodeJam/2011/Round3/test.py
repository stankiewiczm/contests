F1 = open("A-large.out",'r')
F1 = open("test.out",'r');
F2 = open("A-large.bruce",'r')

while True:
	S1 = F1.readline()[0:-1]#.split()[0];
	S2 = F2.readline()[0:-1]#.split()[0];
	if len(S1) == 0:
		break;
	if S1[0] == 'C':
		if S1 != S2:
			print S1, S2
	else:
		f1 = float(S1);		f2 = float(S2);
		if abs(f1-f2) > 1e-6:
			print f1, f2
#	print F1.readline()

