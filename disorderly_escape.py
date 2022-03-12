from fractions import gcd

def solution(w,h,s):
    l=partitions(max(w,h))
    part_w=l[w-1]
    part_h=l[h-1]
    print(part_w,part_h)
    sum=0
    for p1 in part_w:
        for p2 in part_h:
            temp=0
            #number of permutations whoose partition is p1
            n1=fctrl(w)
            for i,j in enumerate(p1):
                n1=n1//( ((i+1)**j)*fctrl(j) )
            n2=fctrl(h)
            for i,j in enumerate(p2):
                n2=n2//( ((i+1)**j)*fctrl(j) )
            
            for c1_size,times1 in enumerate(p1):
                for c2_size,times2 in enumerate(p2):
                    temp+=times1*times2*gcd(c1_size+1,c2_size+1)
            sum+=n1*n2*int(s**temp)
    return sum//(fctrl(w)*fctrl(h))

def fctrl(n):
    if(n==0): return 1
    prod=1
    for i in range(1,n+1):
        prod*=i
    return int(prod)


def partitions(n):

    #a partition is a tuple of n elements
    # (i1,i2,i3,...,in)
    # it contains: i1 1's, i2 2's, i3 3's etc.

    l=[]
    #l is gonna fill with sets of all partitions of 1,2,...,n

    #partition of 1
    p=(1,)
    for _ in range(n-1):
        p+=(0,)
    #print(p)

    l.append({p})

    def add_partitions(p1,p2):
        newp=()
        for i in range(n):
            newp+=(p1[i]+p2[i],)
        return newp
    
    #print(add_partitions((0,1,2,3,4),(4,2,3,5,2)))

    for i in range(1,n):
        #find partitions of i+1
        
        #1st and obvious partition
        p=()
        for j in range(n):
            p+=(1,) if j==i else (0,)

        #print(p)
        newset=set()
        newset.add(p)

        for j in range((i+1)//2):
            #use j, i-j and combine them
            for p1 in l[j]:
                for p2 in l[i-j-1]:
                    #print(p1,p2)
                    newset.add(add_partitions(p1,p2))

        l.append(newset)
    return l

print(solution(2,3,4))