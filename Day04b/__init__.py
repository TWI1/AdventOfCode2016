
import string

#predefined lists
letters_list=list(string.ascii_lowercase)
digits_list=list(range(10))
ignore_list = ["-", "'","["]
end_char="]"


#Returns the list of triples parsed from file input 
def parse_file(file_name):
    with open(fname) as f:
        file_input = f.readlines()
        
        
    return file_input
    #return output

def process_room_record(record):
    #print('Record: ',record)
    encountered_letters=[]
    encountered_letters_counts=[]
    room_id=[]
    checksum=[]
    reading_checksum=False
    room_name=[]
    for l in record:
        #print("Processing letter ", l, ":")
        if l in ignore_list:
            if reading_checksum==False:
                room_name.append(l)
            pass
        elif l in letters_list:
            if not reading_checksum:
                room_name.append(l)                
                if l in encountered_letters:
                    ind=encountered_letters.index(l)
                    encountered_letters_counts[ind]=encountered_letters_counts[ind]+1
                else:
                    encountered_letters.append(l)
                    encountered_letters_counts.append(1)
            else:
                checksum.append(l)
        elif l==end_char:
            break        
        elif int(l) in digits_list:
            reading_checksum=True
            room_id.append(l)
        else:
            break
    
    room_name = ''.join(room_name)
    #room_id = int(room_id)
    #print('Room name: ', room_name)    
    #encountered_letters_copy=encountered_letters.copy()
    
    #DIAG
    #print("encountered letters:",encountered_letters)
    #print("encountered letter counts:",encountered_letters_counts)
    #print("room ID:",room_id)
    #print("checksum:",checksum)
    
    #verify checksum
    #-went through the list and:
    #    -when encountering larger number, note it and start new array of val indexes
    #    -when encountering the same number, add its index to the array
    #    -if one member of index array, just find the right letter and add it to the constructed checksum
    #    -if multiple occurrences, sort those letters alphabetically, and add them to the the constructed checksum
    #    -if constructed checksum corresponds to the provided checksum, room is real -> add the room number to the total
    
    
    constructed_checksum=[]
    
    while encountered_letters_counts:
        
        max_val=0
        max_val_index_array=[]
        
        for i in range(len(encountered_letters_counts)):
            
            #if new maximum, note it & clear and init index aray
            if encountered_letters_counts[i]>max_val:
                max_val=encountered_letters_counts[i]
                max_val_index_array.clear()
                max_val_index_array.append(i)            
            #if existing maximum, just add it to the array
            elif encountered_letters_counts[i]==max_val:
                max_val_index_array.append(i)
                
            
        #now we have a maximum value and array of indexes of it's occurrences 
        #we need to sort the corresponding letters alphabetically
        
        max_val_letters=[]
        
        #fill in the max_val_letters array
        for i in max_val_index_array:
            max_val_letters.append(encountered_letters[i])
        
        #print ("Max_val_letters: ", max_val_letters)
        
        #remove the values from the original array 
        for i in max_val_letters:
            encountered_letters.remove(i)
            encountered_letters_counts.remove(max_val)
        
        #finally, sort the max_val_letters array alphabetically and add it to constructed_checksum 
        max_val_letters.sort()
        for i in max_val_letters:
            constructed_checksum.append(i)
        
    #print ("Constructed checksum: ", constructed_checksum)
    #print ("Part checksum: ", constructed_checksum[:5])
    
    if constructed_checksum[:5]==checksum:
        #print("Real room!")
        room_id = ''.join(room_id)
        room_id = int(room_id)
        #print(encountered_letters_copy)
        rotation_number=room_id%26
        rotated_room_name=alphabet_rotation(room_name, rotation_number)
        print('***********************')
        print('Room name: ', room_name)
        print('Rotated room name: ', rotated_room_name)
        print('Room ID: ', room_id)
        return room_id
    else:
        return 0

def process_rooms_intput(input):
    sum_of_real_room_id=0
    for i in input:
        sum_of_real_room_id=sum_of_real_room_id+process_room_record(i)
    return sum_of_real_room_id

def alphabet_rotation(str, shift):
    alphabet=string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    dash='-'
    space=' '
    alphabet=alphabet+dash
    shifted_alphabet=shifted_alphabet+space       
    table = str.maketrans(alphabet, shifted_alphabet)
    return str.translate(table)
 
#parse record
#take next char
#if dash or ', ignore it
#if a letter, check whether it's already in the letter_list - if yes, just increase it's counter, if no, add it and set the counter to 1
#if a number, add to id part
#if '[', put next 5 chars to a checksum
#sector id processing
#if '[', read letters until ']' and add them to checksum
#after the checksum is read, verify the record is valid - if so, add the room id to the sum 
# ========================================== program

#Get the output
fname='/media/stor_main/!0_Projekty/!0_Dev/AdventOfCode2016/input04.txt'
input=parse_file(fname)

sum=process_rooms_intput(input)
print(sum)
#id_sum=0
#print("Record 0: ", input[0])
#a=process_room_record(input[0])

#str='a'
#print(int(str)+1)
str='a-b-c-x'
shift=2

print(alphabet_rotation(str, shift))
#print(a)
#print(a+1)
#for i in input:
#    id_sum=id_sum+process_room_record(i) 
    
    
    
#Part B
#https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python