def solution(s):
    # Your code here
    l=len(s)
    min_period=l
    for i in range(l,0,-1):
        if(l%i==0):
            #print(i,'is a possible period')
            if(check_period(i,s)):
                #print(i,'is a good period')
                min_period=i
    return l//min_period;

def check_period(p,s):
    #print('initial segment',s[0:p])
    for k in range(0,len(s)//p):
        #print(s[k*p:(k+1)*p])
        if(s[k*p:(k+1)*p]!=s[0:p]): return False
    return True


print(solution("abcabcabcabc"))