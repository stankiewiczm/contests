from numpy import *

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


def Solve(target, foodList):
    for j in [x for x in powerset(range(len(foodList)))]:
        value = array([0,0,0]);
        for index in j:
            value += foodList[index];

        if value[0] == target[0]:
            if value[1] == target[1]:
                if value[2] == target[2]:
                    return "yes";
    return "no";
              

T = int(raw_input());
for q in range(T):
    Target = array(map(int, raw_input().split()));
    N = int(raw_input());
    FoodList = [];
    for n in range(N):
        FoodList.append( array(map(int, raw_input().split())) );

    print "Case #%d:" % (q+1),
    print Solve(Target, FoodList);


