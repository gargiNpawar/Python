count=1
while count<=5:
    print("hello",count)
    count+=1
    
i=1
while i<=5:
    print(i)
    i+=1

i=5
while i>=1:
    print(i)
    i-=1

i=1
while i<=100:
    print(i)
    i+=1

i=100
while i>=1:
    print(i)
    i-=1

i=1
n=int(input("Enter a number:"))
while i<=10:
    print(n*i)
    i+=1

i=1
while i<=10:
    print(i*i)
    i+=1

nums=[1,4,9,16,25,36,49,64,81,100] #list
idx=0
while idx<len(nums):  #traverse
    print(nums[idx])
    idx+=1
print(len(nums))

   
nums=(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while i<len(nums):  #len(nums)=10
    if(nums[i]==x):
        print("Found x at:",i)
    i+=1  


#BREAK AND CONTINUE   
nums=(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while i<len(nums):  #len(nums)=10
    if(nums[i]==x):
        print("Found x at:",i)
        break  #terminates the loop
    else:
        print("FINDING...")    
    i+=1   

i=1
while i<=5:
   print(i)
   if(i==3):
       break 
   i+=1
 
i=0
while i<=5:
   if(i==3):
       i+=1
       continue #for skipping..where it goes back to the loop
   print(i)
   i+=1
    
i=1   #print only odd nos
while i<=10:
    if(i%2==0):
        i+=1
        continue    
    print(i)
    i+=1



#FOR LOOP
nums=[1,2,3,4,5]
for val in nums:
    print(val)


str="apnacollege"
for  char in str:
    if(char=="o"):
        print("Found o")
        break

    print(char)  
print("END OF LOOP")


list=[1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val)


nums=(1,4,9,16,25,36,49,64,81,100,49)  #LINEAR SEARCH
x=49
idx=0
for el in nums:
    if(el==x):
        print("Element found at",idx)
    idx+=1


nums=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for el in nums:
    if(el==x):
        print("Element found at",idx)
        break
    idx+=1
print(idx)  #after break comes to this statement


#RANGE IN LOOPS

for i in range(101): #101 not included....1 to 100
    print(i)

for i in range(100,0,-1): #100 to 1...decrease by 1(-1)
    print(i)   

n=int(input("Enter a Number:"))
for i in range(1,131):
    if(i%n==0):
        print(i)  

        #OR
n=int(input("Enter a Number:"))
for i in range(1,11):
    print(n*i)


sum=0
i=1
n=int(input("Enter how many nos to be calculated:"))
while i<=n:
    sum=sum+i
    i+=1
print(sum)    
         #OR
n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


fact=1
i=1
n=5
while i<=n:
    fact=fact*i
    i+=1
print(fact)

n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of nos=",fact)
