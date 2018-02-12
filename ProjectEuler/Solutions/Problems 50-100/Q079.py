File = open('../TXTdata/keylog.txt','r');

Prior = [ [], [], [], [], [], [], [], [], [], [] ];
Nums = [ ];

for n in range(50):
    key = int(File.readline());
    a = key/100;        b = (key/10)%10;        c = key%10;
    if b not in Prior[a]:
        Prior[a].append(b);
    if c not in Prior[a]:
        Prior[a].append(c);
    if c not in Prior[b]:
        Prior[b].append(c);


for k in range(10):
    Nums.append(len(Prior[k]));

while max(Nums) > 0:
    m = Nums.index(max(Nums));
    print m,;
    Nums[m] = 0;
print Prior[m][0];
