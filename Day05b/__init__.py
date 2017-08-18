import string
import hashlib

# -------------------------------------------- constants

#my_string='abc'         #test
my_string='abbhdwsy'     #real thing

# -------------------------------------------- functions for calculating the password

def return_password(letters, num_of_digits):
    counter=0
    password=[]
    while(len(password)<num_of_digits):
        letters_with_count=letters+str(counter)    
        letters_with_count_hashed=hashlib.md5(letters_with_count.encode()).hexdigest()
        if letters_with_count_hashed[:5]=='00000':
            password.append(letters_with_count_hashed[5:6])
        counter=counter+1
    return password
                        
# ========================================== program

print(''.join(return_password(my_string, 8)))