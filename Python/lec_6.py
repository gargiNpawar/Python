def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(4,6)

#OR

def calc_sum(a,b): #function definition...a,b paramters
    return a+b
sum=calc_sum(6,7) #function call...1,2 arguments
print(sum)

def print_hello():
    print("Hello")
print_hello() 
print_hello()
print_hello()   

ouput=print_hello()
print(ouput)  #prints none as nothing is returned

def avg_nos(a,b,c):
    avg=a+b+c/3
    print(avg)

avg_nos(1,3,4)   

def cal_prod(a=1,b=1): #default parameter
   product=a*b
   print(product)
   return product
cal_prod()

def cal_prod(a,b=1):
   product=a*b
   print(product)
cal_prod(2)

#FACTORIAL
nums=[2,3,4,6,89,22,55,67,87] #to print the length of function
def list_length(list):
    print(len(list))
list_length(nums)    


heros=["batman","spiderman","gogo","hustlepuppy","tomboy"]  
def print_list(list):  #to print the list in the same line
    for el in list:
        print(el,end=" ")
print_list(heros)


def fact_num(n):  #print factorial
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact_num(6)      


def converter(usd_val):   #conversion 
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")
converter(22)    

def string_reco():
    num=int(input("ENTER A NUMBER :"))
    if(num%2==0):
        print(num,"is EVEN")
    else:
        print(num,"is ODD")
string_reco()            

#RECURSSION....when the function calls itself
def show(n):
    print(n)
show(5)    

def show(n):
    if(n==0): #this is base case...condition for stopping
        return #n=0 layer gets deleted and returns to n=1 layer...one by one after each work is done layer wise and each layer gets deleted
    print(n)    #it act as a loop
    show(n-1)  #function calling itself...it start the function call again
    print("END") #last piece of work of each layer while returning

show(5) #output is 5 4 3 2 1  
#first..n=5..check condition..print 5..then functionn call of n=4...loop starts and same process stack by stack

"""
n=0 stack of calls 
n=1 end1 printed
n=2 end2 printed
n=3  ..
n=4  ..
n=5  ..
"""
#n! = (n-1)! * n  ....its recursion where n!(bigger) is dependent on its smaller version...recurence relation
# 1!==0!==1

def fact(n):
    if (n==1 or n==0): #base case
        return 1
    else:
       return fact(n-1)*n
print(fact(4))   

"""
fact(0)...returns 1
fact(1)...1*1=1
fact(2)...1*2=2
fact(3)...2*3=6
fact(4)...6*4=24..final value of 4!
"""
#sum of n natural nos
def calc_sum(n):
    if(n==0):
        return 0
    else:
        return calc_sum(n-1)+n #sum(5)=sum(4)+5
sum=calc_sum(5)
print(sum)   

"""
sum(0)...returns 0
sum(1)...0+1=1
sum(2)...1+2=3
sum(3)...3+3=6
sum(4)...6+4=10
sum(5)...10+5=15..final answer of 1+2+3+4+5
"""

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","lichi","apple","banana","watermelon"]
print_list(fruits)    

#first we print idx=0 if idx!=5 ie print mango then idx=0+1=1..then we print lichi...index increase by one everytime