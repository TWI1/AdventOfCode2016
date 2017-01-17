
#get the input 
#create a method Solver - input is a list of doubles - direction and length, output is a number of blocks
#global vars - x, y, direction
#if direction is 0 (north), I'm adding to x
#if direction is 1 (east), I'm adding to y
#if direction is 2 (south), I'm subtracting from x
#if direction is 3 (west), I'm subtracting from y
#for R -> direction=direction+1
#for L -> direction=direction-1
#I may use a division reminder of direction / 4

#Done:
#*put into it into array or List
#*add code to calculate taxiCabDistance

input="R1, L2, R3"
input2="R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"

def parse_input(input):    
    list=[x.strip() for x in input.split(',')]
    doubles=[]
    for i in list:
        doubles.append((i[0],i[1:]))
    return doubles 

def day0_solver(input):
    x=0
    y=0
    direction=0
    path=[]
    crossSections=[]
    
    path.append([x,y])
        
    for i in input:
        if i[0]=='R':
            direction=direction+1
        else: #=='L'
            direction=direction-1
            
        for j in range(int(i[1])):
            
            if direction%4==0:
                x=x+1
            elif direction%4==1:
                y=y+1
            elif direction%4==2:
                x=x-1
            else:
                y=y-1
            
            if ([x,y] in path):
                crossSections.append([x,y])
                
            path.append([x,y])
    
    crossSectionsDistances=[]
        
    for i in crossSections:
        crossSectionsDistances.append(abs(i[0])+abs(i[1]))
                            
    return [abs(x)+abs(y), crossSectionsDistances]


l=parse_input(input2)
print(day0_solver(l))