def solution(pegs):
    n=len(pegs)
    f=2+(-1)**n
    sum=-pegs[0]
    for i in range(1,n-1):
        sum+=2*((-1)**(i+1))*pegs[i]
    sum+=((-1)**n)*pegs[n-1]

    #first gear radius = 2*sum/f
    #print('f',f)

    if sum<=0:
        #print('sum negative')
        return -1,-1
    else:
        a=2*sum
        b=f

        #check gears length
        r=a/b
        #print('gears length')
        #print(r)
        for i in range(n-1):
            r=pegs[i+1]-pegs[i]-r
            #print(r)
            if(r<0): return -1,-1

        #simplify
        if a%f==0:
            a=int(a/f)
            b=int(b/f)
    return a,b

print(solution([4,30,50]))