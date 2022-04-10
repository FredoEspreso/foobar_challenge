from math import sqrt
from decimal import *
getcontext().prec = 110
s='1.4142135623730950488016887242096980785696718753769480731766797379907324784621'
s+='07038850387534327641572735013846230912297024924836055850737212644121497099935831'
s=s[:110]
sq2=Decimal(s)
def solution(s):
    n=int(s)
    return str(beatty_sum(n))

def beatty_sum(n):
    if(n<5):
        return sum([int(i*sqrt(2)) for i in range(n+1)])
    else:
        k=int(sq2*n)
        m=int(n*(sq2-1))
        return k*(k+1)//2-m*(m+1)-beatty_sum(m)


print(solution('77'))
