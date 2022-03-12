def solution(l):
    #kinda fast
    length=len(l)
    count=0
    
    d=[]
    for i in range(length):
        d.append([])
        for j in range(i+1,length):
            if(l[j]%l[i]==0):
                d[i].append(j)
    #print(d)

    for i in range(length):
        for index in d[i]:
            count+=len(d[index])

    return count

print(solution2([1, 2, 3, 4, 5, 6]))