
keypad = [1,2,3,4,5,6,7,8,9]
inp=['LLULLLRLDLLLRLUURDDLRDLDURULRLUULUDDUDDLLLURRLDRRLDRRRLDUDLRDLRRDLLDUDUDUDRLUDUUDLLLRDURUDUULUDLRDUUUDUUDURLDUULLRDLULDUURUDRDDLDRLURLRURRDUURLRLUURURUUULLRLLULRUURLULURDLLRRUDLUDULDRDRLRULUURRDRULLRUUUDLRLDLUURRRURDLUDDRRUDRLUDRDLLLLLRULLDUDRLRRDDULDLRUURRRRRLDLDLRDURDRUUURDLRDDDDULURRRRDUURLULLLDLRULRDULRUDLRRLRDLLRLLLUDDLRDRURDDLLLLDUDRDLRURRDLRDDDLDULDRLRULUUDRRRUUULLLURRDDUULURULDURRLLULLDRURUUULRLRDRRUDRDRRDURRUUUULDRDDDUDLDDURLLRR',
'LDLRRRUURDLDDRLRRDLLULRULLLUDUUDUDLRULLDRUDRULLDULURDRDDLRURDDULLLLDLRDRDRDDURLURLURLUDRDDRDULULUDDRURRDLLDUURDRDDLRLLURRDLRDDULDLULURDRDLUDRRUUDULLULURRDUDRUUUDRULDLDURLRRUDURLDLRRUURRRURDLUDRLDUDRRUDUURURUDDUUDRDULRDLUDRRRLDRURLLRDDDLUDRDUDURDDDRRDDRRRLLRRDDLDDLRUURRURDLLDRLRRDLLUDRRRURURLRDRLLRLRLRULLRURLDLRRULLRRRDULUUULDRDLLURDDLDLRDRLUUDLLUDDLDRRLDLRUDRUDLLUURLLULURUDUDRLULLUDRURDDLDLDDUDLRDDRRURLRLLUDDUDRUURRURRULDRLDDRLLRRLDDURRDLDULLLURULLLRUURLRRRRUUULRLLLURRLRLRUDRDUUUDUUUDDLULLDLLLLDLDRULDRUUULDDDLURLDLRLULRUDDDDURDDLU',
'RURLURRDLDULLULDDDLRUULLUURLRUDRUDRRUDDLDDDDRRDLRURLRURLDDDUDDUURRDRULDRRRULRDRDDLRUDULRLURDUUDRRLDLRDRURDLDRRRRDRURUUDDDLLRDRDUDUDUDLLULURULRRLRURUULUULDDDDURULRULLRUDUURLURDUDLUDLUDRLLDUUDUULRLRLUUDRDULDULRURDRRRULRUDLRURDDULUDULLRLRURURUULLULDRURLLRRUUDDUUURRDLURUURULRDRRDDUDULRDDLUDLURURUURDRULLRDDLLRDDLDRDUDRRDLUURRLRLUURRULUDURLDDRLLURRDDDLDDRURULLDDRLUDDLRLURDUDULLRDULLLDLLUDDRUDRUDDUUDRDRULRL',
'RLRDRDULULUDLUDRDRLUDLDLLUDURULDDDUDLRURLLRLRLDLDRLDURDLRRURLULLULURLLDRRDRLUDRLRDLLULRULURRURURUULRDUDLLRDLRRRRRLUURDRRRDLRUDLLDLLDLRUUUDLLLDDDLRDULLRUUDDRLDDURRRDLRLRLDDDDLRDRULLUURUUDRRLLRLLRDDLLRURRRRDRULRRLLRLLLRLDRRLDDDURRURLDURUURRLRLRLDRURULLRLRUDLDUURDLLRLDLURUUUDLLRDRDDDDDDRLDRRRLRRRRURUDLDDRDLLURUDLRRLDDDLUDUDUULRDULULUDDULUUDLLLLRLDDUUULRLRDULURDURRRURRULURRRDRDLDDURDLURUDURRRDDRLRLUDLUDDLUULLDURLURDDUDDLRUUUDRLLDRURL',
'ULUDLLUDDULRUURDRURDUDUDLUURDDDRRLUDURURDRURRLDRDURLRLLRRDDRRDRRRUULURUDURUDULRRRRDDLDURRLRRDUDDDRLLLULDRLRLURRDUURDURRRURRDLUDUDDRLDLURRRDDRLLRDRDDRDURRRRLURRLUDDURRULRUDUDULDRUDDRULLUUULDURRRLDRULLURULLRUDLDUDDLDULDLUUDRULULDLLDRULLRUULDUDUUDRLRRLDLUULUDLLDDRLRRDDLLURURDULRRDDRURDRLRLULDLDURULLUUUDURURDLDUDDDDUUULUDLUURRULLDLRLURDLURLRLDDURRLDDRRRDUUULLUULDLLDLLDDRLRRUDLULDRLULDULULRRLRULUUURURUUURDUUDDURLLUDDRLRDDLUURRUULRDLDDRLULUULRDRURLUURDRDUURUDLRR']

inp0='LURDD'

inp1=['LURDD','RUULLL','DDUDD','RU','RRRRRDRRR']

inp2=['ULL','RRDDD','LURDL','UUUUD']

#print(inp)
#print(keypad)

#1,2,3
#4,5,6
#7,8,9

def return_key(x, y):
#Converts coords to key on numeric keyboard    
    if x==0 and y==0: return 7
    if x==1 and y==0: return 8
    if x==2 and y==0: return 9

    if x==0 and y==1: return 4
    if x==1 and y==1: return 5
    if x==2 and y==1: return 6

    if x==0 and y==2: return 1
    if x==1 and y==2: return 2
    if x==2 and y==2: return 3
        
def return_coords(key):
#Converts key on numeric keyboard to coords
    if key==7: return (0,0)
    if key==8: return (1,0)
    if key==9: return (2,0)

    if key==4: return (0,1)
    if key==5: return (1,1)
    if key==6: return (2,1)

    if key==1: return (0,2)
    if key==2: return (1,2)
    if key==3: return (2,2)
    
def process_coords(x,y, seq):
    for i in seq:
        if i=='L':
            if x>=1: x=x-1
        if i=='R':
            if x<=1: x=x+1
        if i=='U':
            if y<=1: y=y+1
        if i=='D':
            if y>=1: y=y-1
        
    return return_key(x,y)


fname='/media/stor_arch/TEMP!!!/input.txt'
with open(fname) as f:
    content = f.readlines()
    
for i in content:
    print(i)           
               
keyseq=[]

#for i in inp:
for i in content:
#for i in inp2:
    if keyseq==[]:        
        keyseq.append(process_coords(1,1,i))
    else:
        previous_coords=return_coords(keyseq[-1])        
        keyseq.append(process_coords(previous_coords[0],previous_coords[1],i))
        
print(keyseq)        


