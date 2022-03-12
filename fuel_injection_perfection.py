#operations: 1. add 1, 2. remove 1, 3. divide with 2 (even)

def solution(n):
    d={"1":0,"2":1}
    while True:
        dict_update={}
        for num in d:
            if(num==n):
                return d[num]
            m=int(num)
            if(str(m+1) not in d.keys()):
                dict_update.update({str(m+1):d[num]+1})
            if(m-1>1 and str(m-1) not in d.keys()):
                dict_update.update({str(m-1):d[num]+1})
            if(str(2*m) not in d.keys()):
                dict_update.update({str(2*m):d[num]+1})
        d.update(dict_update)
        #print(d)

def solution2(n):
    d1={"1":0,"2":1} #dict with all minimum costs
    d2={"2":1} #temporary dict only for nth step with numbers of cost n
    cost=1
    while True:
        d_add={}
        cost+=1
        for num in d2: #explore only in d2
            m=int(num)
            for num2 in [str(m+1),str(m-1),str(2*m)]:
                if num2 not in d1.keys():
                    d_add.update({num2:cost})
            
        if(n in d_add):
            return d_add[n]

        d1.update(d_add)
        d2=d_add

        #print(d1)
        #print(d2)

def solution3(n):
    # Mark all the vertices as not visited
    visited = {"1":0,"2":1}

    # Create a queue for BFS
    queue = ["2"]

    # Mark the source node as 
    # visited and enqueue it

    while True:

        # Dequeue a vertex from 
        # queue and print it
        #print(queue)
        s = queue.pop(0)
        #print (s, end = " ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        num=int(s)
        cost=visited[s]
        for i in [str(num-1),str(num+1),str(2*num)]:
            if i not in visited:
                if(i==n): return cost+1
                queue.append(i)
                visited[i] = cost+1

def solution4(n):
    t=n
    b=bin(int(n))
    steps=0
    while True:
        steps+=1
        if(b[-1]=='0'):
            t=int(b,2)//2
        elif(b==bin(3) or b[-2:]=='01'):
            t=int(b,2)-1
        else:
            t=int(b,2)+1
        #print(t)
        b=bin(t)
        if(t==1):
            return steps


def solution5(n):
    temp=int(n)
    steps=0
    while True:
        a=temp%4
        steps+=1
        if(a==0 or a==2):
            temp=temp//2
        elif(temp==3 or a==1):
            temp-=1
        else:
            temp+=1
        #print(t)
        if(temp==1):
            return steps

print(solution5("15"))