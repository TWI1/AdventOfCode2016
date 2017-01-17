
import string

#Test inputs
inp0='LURDD'
inp1=['LURDD','RUULLL','DDUDD','RU','RRRRRDRRR']
inp2=['ULL','RRDDD','LURDL','UUUUD']
inp3=['L','U','R','DD']

#1,2,3
#4,5,6
#7,8,9


#X=01234  Y
#         =
#4   1    4
#3  234   3
#2 56789  2
#1  ABC   1
#0   D    0
#=
#Y
#X=01234
#allowed coords:
#(0,2),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2)(3,3),(4,2)

# -------------------------------------------- Keypad class

class keypad:
    
    allowed_positions = []
    keys = []
    center= []
        
    #Checks if coordinates are allowed for the keypad
    def is_coords_allowed(self, coords):
        if coords in self.allowed_positions:
            return True 
        else:
            return False
    
    #Convert coords2key 
    def return_key(self, coords):
        if coords in self.allowed_positions:
            ind=self.allowed_positions.index(coords)        
            return(self.keys[ind])
        else:
            return

    #Convert key2coords
    def return_coords(self, key):        
        if key in self.keys:    
            ind=self.keys.index(key)        
            return(self.allowed_positions[ind])
        else:
            return
            
    #Constructs a list of keys on a keypad
    def construct_list_of_keys(self):
        #Construct the list of keys
        
        if self.allowed_positions==[]:
            return
         
        available_keys=list(range(1,10))    #Include all the digits            
                           
        if len(self.allowed_positions)>9:   #If more than 9 keys, include all the letters
                available_keys=available_keys+list(string.ascii_uppercase)
            
        if len(self.allowed_positions)>35:   #If more than 35 keys, include numbers starting at 11
                available_keys=available_keys+list(range(11,11+len(self.allowed_positions)-35))
            
        self.keys=available_keys[:len(self.allowed_positions)]        
    
# -------------------------------------------- Rectangle-shaped keypad class

class keypad_rectangle(keypad):
  
    allowed_positions = []
    keys = []
    center= []
    
    def __init__(self, rows_count, columns_count):
        
        #Construct the list of allowed positions
        self.construct_list_of_allowed_positions(rows_count, columns_count)
        
        #Construct the list of keys
        self.construct_list_of_keys()
                                
        #Calculate the center
        self.construct_center(rows_count, columns_count)
                            
        #print(self.allowed_positions); print(len(self.allowed_positions)); print(self.keys); print(self.center)    #DIAG
        
        return
    
    #Create a list of allowed positions on the keypad
    def construct_list_of_allowed_positions(self, rows_count, columns_count):
        for i in range(rows_count):
            for j in range(columns_count):
                self.allowed_positions.append((i,j))
    
    #Create a center of the keypad            
    def construct_center(self, rows_count, columns_count):
        self.center=((rows_count-1)/2, (columns_count-1)/2)
                
# -------------------------------------------- Diamond-shaped keypad class

class keypad_diamond(keypad):

    allowed_positions = []
    keys = []
    center= []
          
    def __init__(self, rows_count):
        if rows_count%2==1:             #Is rows count an odd number? If yes, proceed with constructing the object
            
            #Construct the list of allowed positions
            self.construct_list_of_allowed_positions(rows_count)
            
            #Construct the list of keys
            self.construct_list_of_keys()
                                    
            #Calculate the center
            self.construct_center()            
                    
            #print(self.allowed_positions); print(len(self.allowed_positions)); print(self.keys); print(self.center)    #DIAG
        
        return

    #Create a list of allowed positions on the keypad
    def construct_list_of_allowed_positions(self, rows_count):
        for i in range(rows_count):
            if i <= ((rows_count-1)/2):     #Construct 1st half of rows + the central one
                for j in range( int(((rows_count-1)/2))-i ,int(((rows_count-1)/2)+1)+i):
                    self.allowed_positions.append((i,j))
            else:                           #Construct 2nd half of rows
                for j in range( int(((rows_count-1)/2))+i-rows_count+1,int(((rows_count-1)/2)+1)-i+rows_count-1):    
                    self.allowed_positions.append((i,j))
                    
    #Create a center of the keypad
    def construct_center(self):
        self.center=self.allowed_positions[int((len(self.allowed_positions)+1)/2)-1]
        
# -------------------------------------------- functions for solving the puzzle

def process_coords(x,y, keypad, seq):
    for i in seq:
        if i=='L':            
            if keypad.is_coords_allowed((x,y-1)):
                y=y-1
        if i=='R':            
            if keypad.is_coords_allowed((x,y+1)):
                y=y+1
        if i=='U':            
            if keypad.is_coords_allowed((x-1,y)):
                x=x-1
        if i=='D':            
            if keypad.is_coords_allowed((x+1,y)):
                x=x+1
        
    return keypad.return_key((x,y))


def solve_keypad_puzzle(keypad, sequences):
    keyseq=[]
    for i in sequences:
        if keyseq==[]:            
            keyseq.append(process_coords(keypad.center[0],keypad.center[1],keypad,i))
        else:
            previous_coords=keypad.return_coords(keyseq[-1])
            keyseq.append(process_coords(previous_coords[0],previous_coords[1],keypad,i))
            
    return keyseq  

# ========================================== program

#Get the output
fname='/media/stor_arch/TEMP!!!/input.txt'
with open(fname) as f:
    input = f.readlines()

#Solve 2a
keypad1=keypad_rectangle(3,3)
solution1=solve_keypad_puzzle(keypad1, input)
print(solution1)

#Solve 2b
keypad2=keypad_diamond(5)
#b=solve_keypad_puzzle(a, inp1)    #DIAG
solution2=solve_keypad_puzzle(keypad2, input) 
print(solution2)


