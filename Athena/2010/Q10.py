from numpy import *


#[(83^{2^(649948729)*5^(99)}) * 103^{21}]%160001

A2 = (103**21)%160001

#83 has period 160000 mod 160001
# so the first term is 1 mod 160001

print A2;
