
#Returns True if triple is a triangle, or false if it is not
def is_triangle(triple):
    if triple[0]+triple[1]>triple[2] and triple[0]+triple[2]>triple[1] and triple[1]+triple[2]>triple[0]:
        return True
    else:
        return False 

#Returns the list of triples parsed from file input 
def parse_file(file_name):
    with open(fname) as f:
        file_input = f.readlines()    
        intermediate_output=[x.strip() for x in file_input]    
        output=[]
        for i in intermediate_output:
            x=i.split()
            output.append((int(x[0]),int(x[1]),int(x[2])))
    return output

#Returns the number of triangles in rows for a specified list         
def number_of_triangles_in_rows(input):
    count=0

    for i in input:
        if is_triangle(i):
            count=count+1
            
    return count

#Returns the number of triangles in columns for a specified list
def number_of_triangles_in_columns(list_old):
    count=0
    list_new=list_old.copy()
    
    while len(list_new)>0:
        a=list_new.pop()
        b=list_new.pop()
        c=list_new.pop()
        if is_triangle((a[0],b[0],c[0])):
            count=count+1
        if is_triangle((a[1],b[1],c[1])):
            count=count+1
        if is_triangle((a[2],b[2],c[2])):
            count=count+1
    return count

# ========================================== program

#Get the output
#fname='/media/stor_arch/TEMP!!!/input03.txt'
fname='/media/stor_main/!0_Projekty/!0_Dev/AdventOfCode2016/input04.txt'
parsed_input=parse_file(fname)      
#print(parsed_input)                    #DIAG
        
print('Number of triangles in rows: ', number_of_triangles_in_rows(parsed_input))
print('Number of triangles in columns: ', number_of_triangles_in_columns(parsed_input))