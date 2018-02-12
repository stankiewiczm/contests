ways = [0]*101
ways[0] = 1
for i in range(1, len(ways)):
    for j in range(i, len(ways)):
        ways[j] += ways[j-i]
print ways[100]-1
