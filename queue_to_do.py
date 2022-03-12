def solution(start, length):
    len=length
    id=start
    cs=0
    for len in range(length,0,-1):
        for _ in range(len):
            cs=cs^id
            id+=1
        id+=length-len
    #print(cs)
    return cs

def solution2(start,length):
    cs=0
    for k in range(length):
        cs^=xor_ap(start+k*length,start+(k+1)*(length-1))
    return cs

def xor_ap(start,end):
    if(start==0):
        a=end%4
        if(a==0):
            return end
        elif(a==1):
            return 1
        elif(a==2):
            return end+1
        else:
            return 0
    else:
        return xor_ap(0,start-1)^xor_ap(0,end)

print(solution2(17,4))
""" cs=0
for i in range(100):
    cs^=i
    print(i,cs )"""

""" for i in range(5,15):
    print(5,i,xor_ap(5,i)) """