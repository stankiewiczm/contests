import sys, string
rl = lambda: sys.stdin.readline().strip()
#f = open("inp")
#rl = lambda: f.readline().strip()

class Node:
    def __init__(self):
        self.children = {}
        self.terminal = -1

    def insert(self, masks, chars, num):
        if not chars:
            self.terminal = num
        else:
            mask = masks[ord(chars[0]) - ord('a')]
            if mask not in self.children:
                self.children[mask] = Node()
            self.children[mask].insert(masks, chars[1:], num)

def get_masks(word):
    ret = []
    for char in string.lowercase:
        m = 0
        for i in xrange(len(word)):
            m = m * 2 + (1 if word[i] == char else 0)
        ret.append(m)
    return ret

def better(a, b):
    if a[0] > b[0]: return a
    if a[0] < b[0]: return b
    if a[1] < b[1]: return a
    return b

def traverse(node, losses=0):
    if node.terminal != -1:
        return (losses, node.terminal)
    if len(node.children) == 1 and (0 in node.children):
        return traverse(node.children[0], losses)
    best = (-1, -1)
    for mask, children in node.children.iteritems():
        if mask == 0:
            best = better(best, traverse(children, losses+1))
        else:
            best = better(best, traverse(children, losses))
    return best

def solve_order(order):
    # (lost points, number)
    best = (-1, -1)
    for length in xrange(1,11):
        root = Node()
        for no in by_length[length]:
            root.insert(get_masks(words[no]), order, no)
        best = better(traverse(root), best)
    return words[best[1]]

t = int(rl())
for cc in range(t):
    n, m = map(int, rl().split())
    words = [rl() for i in xrange(n)]

    by_length = [[] for i in xrange(11)]
    for i in xrange(n):
        by_length[len(words[i])].append(i)

    res = []
    for i in xrange(m):
        res.append(solve_order(rl()))
    print "Case #%d:" % (cc+1),
    print " ".join(res)


