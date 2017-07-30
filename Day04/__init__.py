
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
    encountered_letters=[]
    encountered_letters_counts=[]
    room_id=[]
    checksum=[]
    reading_checksum=False
    for l in record:
        print("Processing letter ", l, ":")
        if l in ignore_list:
            pass
        elif l in letters_list:
            if not reading_checksum:
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
        
    #DIAG
    print("encountered letters:",encountered_letters)
    print("encountered letter counts:",encountered_letters_counts)
    print("room ID:",room_id)
    print("checksum:",checksum)
    
    #verify checksum
    #-went through the list and:
    #    -when encountering larger number, note it and start new array of val indexes
    #    -when encountering the same number, add its index to the array
    #    -if one member of index array, just find the right letter and add it to the constructed checksum
    #    -if multiple occurrences, find the respective letters, and sort it alphabetically, and put the respective letters to the the checksum
    #     (make sure you're not going over 5 letters)
    #    -if constructed checksum corresponds to the provided checksum, room is valid -> add the room number to the total
    
    
    for k in encountered_letters_counts:
        max_count=0;
            
        
    return 0

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

id_sum=0
print("Record 0: ", input[0])
process_room_record(input[0])
#for i in input:
#    id_sum=id_sum+process_room_record(i) 
    
print(id_sum)