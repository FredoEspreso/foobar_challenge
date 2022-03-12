def solution(g):
    h=len(g)+1
    w=len(g[0])+1
    pr=give_rows(h) #all possible ways to fill 1st row
    #print(first_row)
    for r in pr:
        r[0]=1
    #print(pr)

    for i in range(w-1):
        t_pr=give_rows(h)
        for i1 in range(2**h): #[prev_num,prev_row] in pr: #for all possible solutions of previous row
            prev_row=pr[i1][1]
            for i2 in range(2**h):# [new_num,new_row] in t_pr: #for all possible solutions of this row
                new_row=t_pr[i2][1]
                works=True
                for j in range(h-1):
                    if(g[j][i]): works= works and prev_row[j]+prev_row[j+1]+new_row[j]+new_row[j+1]==1
                    else:   works= works and prev_row[j]+prev_row[j+1]+new_row[j]+new_row[j+1]!=1
                if(works):
                    #print('works')
                    #print(prev_row)
                    #print(new_row)
                    t_pr[i2][0]+=pr[i1][0]
        pr=t_pr
        #print(i)
    sum=0
    for k in pr:
        sum+=k[0]
        #print(k)

    print(sum)
    return sum

        

def give_rows(h):
    l=[]
    for i in range(2**h):
        b=[int(j) for j in bin(i)[2:]]
        t=[0]*(h-len(b))+b
        l.append([0,t])
    return l

#print(all_cases_for_row(5))
#print(check(False,0,0,0,0))
#solution([[True, False, True], [False, True, False], [True, False, True]])
solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])