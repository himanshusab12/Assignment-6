#Whether a nuber is perfect or not
a = int(input("Enter a number"))
j=1
Sum = 0
while j<(a//2)+1:
    if(a%j==0):
        Sum+=j
    j+=1
if(Sum==a):
    print("A perfect number")
else:
    print("Not a perfect number")
