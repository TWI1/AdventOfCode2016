import string
import hashlib

# -------------------------------------------- constants

#my_string='abc'         #test
my_string='abbhdwsy'     #real thing

# -------------------------------------------- functions for calculating the password

def return_password(letters, num_of_digits):
    counter=0
    unordered_password=[]
    ordered_password=[]
    indexes=[]
    while(len(unordered_password)<8):
        letters_with_count=letters+str(counter)    
        letters_with_count_hashed=hashlib.md5(letters_with_count.encode()).hexdigest()
        #we're only interested in hashes starting with five zeroes
        if letters_with_count_hashed[:5]=='00000':
            #6th digit between 0..7 is a possition of the letter in password (only first found applies)
            #7th character is the password letter itself
            if letters_with_count_hashed[5:6] in ['0','1','2','3','4','5','6','7']:
                if letters_with_count_hashed[5:6] not in indexes: 
                    indexes.append(letters_with_count_hashed[5:6])                
                    unordered_password.append(letters_with_count_hashed[6:7])                
        counter=counter+1
    #order letters in password according to their indexes specifying position of the letter in word
    for i in range(8):
        ordered_password.append(unordered_password[indexes.index(str(i))])
    return ordered_password
                        
# ========================================== program

print(''.join(return_password(my_string, 8)))