a = input("Enter - separated string")
l = a.split('-')
l.sort()
a=''
for x in l:
    a+=x
    if(x != l[-1]): 
        a+='-'
print(a)
    
    
