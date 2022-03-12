from fractions import Fraction
#import matplotlib.pyplot as plt

def solution(dimensions, your_position, trainer_position, distance):

    #utils-------------------------------------------------
    max_sq_distance=distance*distance

    def check_distance(target):
        if((target[0]-your_position[0])*(target[0]-your_position[0])+(target[1]-your_position[1])*(target[1]-your_position[1])<=max_sq_distance):
            return True
        else:
            return False


    def is_point_in_segment(point,start,end): 

        if(point==start):
            return False

        (x,y)=point
        (x0,y0)=start
        (x1,y1)=end
        x_min=min(x0,x1)
        x_max=max(x0,x1)
        y_min=min(y0,y1)
        y_max=max(y0,y1)

        if(x_min<=x<=x_max and y_min<=y<=y_max):
            return (x1-x)*(y-y0)==(y1-y)*(x-x0)
        else:
            return False
    #------------------------------------------------------


    x_ext=(distance//dimensions[0])+1 #how many boxes we extend left and right
    y_ext=(distance//dimensions[1])+1 #up and down

    #corners
    c1=[0,0]
    c2=[dimensions[0],0]
    c3=[dimensions[0],dimensions[1]]
    c4=[0,dimensions[1]]


    #print(x_ext,y_ext)
    #make reflections
    
    #items to reflect
    items=[trainer_position,your_position,c1,c2,c3,c4]

    ur,ul,dr,dl=[],[],[],[]

    def fill(l,x_end,x_incr,y_end,y_incr):
        for i in range(0,x_end,x_incr):
            l.append([])
            for j in range(0,y_end,y_incr):
                temp=[]
                for k in items:
                    if(i%2==0):
                        if(j%2==0):
                            temp.append([i*dimensions[0]+k[0],j*dimensions[1]+k[1]])    
                        else:
                            temp.append([i*dimensions[0]+k[0],(j+1)*dimensions[1]-k[1]])             
                    else:
                        if(j%2==0):
                            temp.append([(i+1)*dimensions[0]-k[0],j*dimensions[1]+k[1]])   
                        else:
                            temp.append([(i+1)*dimensions[0]-k[0],(j+1)*dimensions[1]-k[1]])  
                l[abs(i)].append(temp)

    fill(ur,x_ext+1,1,y_ext+1,1)
    fill(ul,-x_ext-1,-1,y_ext+1,1)
    fill(dr,x_ext+1,1,-y_ext-1,-1)
    fill(dl,-x_ext-1,-1,-y_ext-1,-1)

    def item_direction(item):
        x=item[0]-your_position[0]
        y=item[1]-your_position[1]

        if(x==0):
            if(y>0):
                return 'u'
            else:
                return 'd'
        else:
            if(x>0):
                return (Fraction(y,x),'r')
            else:
                return (Fraction(y,x),'l')

    used_directions=set()
    count=0

    for quad in [ur,ul,dr,dl]:
        for i in range(x_ext+1):
            for j in range(y_ext+1):
                for item in quad[i][j][1:]:
                    #plt.plot(item[0],item[1],'ro')
                    direction=item_direction(item)
                    used_directions.add(direction)
                clear_path=True
                for item in quad[i][j][1:]:
                    if(is_point_in_segment(item,your_position,quad[i][j][0])):
                        clear_path==False
                if(item_direction(quad[i][j][0]) not in used_directions and clear_path and check_distance(quad[i][j][0])):
                    count+=1
                    used_directions.add(item_direction(quad[i][j][0]))
    return count
    #plt.show()

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))