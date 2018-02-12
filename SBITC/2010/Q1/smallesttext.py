word_lengths=[3,4,4,4,4]
start=max(word_lengths)
end=sum(word_lengths) + len(word_lengths) - 1
col_range=range(start,end+1,1)
endspaces_list=[]
rows_list=[]
for col_width in col_range:
    print col_width
    summy=0
    rows=0
    for i in range(0,len(word_lengths)-1,1):
        endspaces=0
        if summy + word_lengths[i+1] > col_width:
            endspaces = endspaces+(col_width-summy)
            summy=word_lengths[i+1]
            rows=rows+1
        else:
            summy=summy+word_lengths[i+1]+1
    endspaces_list.append(endspaces)
    rows_list.append(rows)

min_endspaces=min(endspaces_list)
indexy=endspaces_list.index(min_endspaces)
bestR=rows_list[indexy]
bestW=col_range[indexy]
print "Case #"+str(1)+": "+str(bestR)+" "+str(bestW)
