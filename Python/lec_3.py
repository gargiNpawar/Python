marks=[98.2,89.0,78.6,55.8]#list
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])
print(marks[0])
#list of python has elements of diff data types

student=["gargi",21,96.2,"mumbai"]
print(student[0])#lists are mutable
student[0]="raj"
print(student[0])
print(student[1:3])
print(student[-4:])

list=[1,2,3,5,4]
list.append(8)#adds to the last
list.sort()#in ascending order
print(list)

list1=[2,6,7,3,4]
print(list1.append(9))#gives output None
print(list1.sort())
print(list1)

list2=["apple","litchi","mango","banana"]
list2.sort(reverse=True)#in descending order
print(list2)
list2.reverse()#reverses the string
print(list2)
list2.insert(1,"cherry")#adds element at a particular index at the reversed list itself
print(list2)

list3=[1,2,1,3,3,2]
list3.remove(2)#removes the first occurence of the element
print(list3)
list3.pop(4)#removes the element at the index
print(list3)


#-------------------------------------------------------------#

tup=(1,)#for tuple , is neccesary otherwise it is a integer
print(tup)
print(type(tup))
#tuple are immutable ie no new elements can be added or changed

tup2=()
print(tup2)
print(type(tup2))

tup1=(1,2,1,3,4)
print(tup1.index(1))#return the index of first occurence
print(tup1.count(1))#counts the total occurences

movies=[]
mov1=input("Enter the first movie:")
mov2=input("Enter the second movie:")
mov3=input("Enter the third movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#OR
movies=[]
mov=input("Enter the first movie:")
movies.append(mov)
mov=input("Enter the second movie:")
movies.append(mov)
mov=input("Enter the third movie:")
movies.append(mov)
print(movies)
#OR
movies=[]
movies.append(input("Enter the first movie:"))
movies.append(input("Enter the second movie:"))
movies.append(input("Enter the third movie:"))
print(movies)

list1=["m","a","r","r","a","m"]
copy_list1=list1.copy()
copy_list1.reverse()
if(list1==copy_list1):
    print("It is a palindrome")
else:
    print("Not a palindrom")    

grade=("a","c","a","d")
print(grade.count("a"))

grade=["a","c","a","d","b"]
print(grade.sort())#returns NONE
print(grade)

