from Numeric import *

PROBS = zeros(1113, Float);

PROBS[1111] = 1.0;      # Pages of size A2, A3, A4, A5;
QUEUE = [1111];         PQ = 0;


def Itr(Qpos):
    V = PROBS[QUEUE[Qpos]];
    OldC = QUEUE[Qpos]
    S = 0;
    for i in str(OldC):
        S += int(i);

    for Card in arange(S):
        Done = 0;       Fig = 10**(len(str(OldC)))
        for i in str(OldC):
            Done += int(i);
            Fig = Fig/10;
            if (Done > Card):
                NewC = OldC - Fig+Fig/9;
                PROBS[NewC] += V/float(S);
                if (NewC not in QUEUE) and (NewC != 1):
                    QUEUE.append(NewC);
                break;  

while PQ != len(QUEUE):
    Itr(PQ);
    PQ += 1;

print PROBS[1000] + PROBS[100] + PROBS[10];
