def Solver(word_lengths, t):
    start=max(word_lengths)
    end=sum(word_lengths) + len(word_lengths) - 1
    #end = 6;
    col_range=range(start,end+1,1)
    endspaces_list=[]
    rows_list=[]
    Area = [999999999]*250;
    for col_width in col_range:
        summy=0
        rows=1
        for i in range(len(word_lengths)):
            if (summy + word_lengths[i] <= col_width):
                summy += (word_lengths[i]+1);
            else:
                summy = word_lengths[i]+1;
                rows += 1;
        Area[col_width] = col_width*rows;

    best = min(Area);
    bestC = Area.index(best);

    print "Case #"+str(t+1)+":",(best/bestC), bestC #+" "+str(bestW)

T = int(raw_input());
for t in range(T):
    words = raw_input();
    list_of_words=words.split(' ')
    word_lengths=[len(word) for word in list_of_words]    
    Solver(word_lengths,t);
#Solver([5,3,4,2,4,1,5],1);
#Solver([13,3,9],2);
