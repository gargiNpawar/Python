f=open("demo.txt","r")  #open the file for reading..where r mode is default
data=f.read()
print(data)   #text mode "t" is also default
print(type(data))
f.close()

f=open("demo.txt","r")
data=f.read(6)
print(data)
f.close()

f=open("demo.txt","rt")  #once the whole reading is done..we cannot read line by line then
line1=f.readline()
print(line1)


line2=f.readline()
print(line2)

line3=f.readline() #empty line gets printed
print(line3)
f.close

f=open("demo.txt","w")  #over-write is done
f.write("I WANT TO LEARN PYTHON FOR ADVANCED LEVEL")
f.close()

f=open("demo.txt","a")  #append ie we add data to existing data at end
f.write("\n I WANT TO LEARN JAVASCRIPT LANGUAGE") #\n sentence to next line
f.close()

f=open("demo.txt","+r") 
f.write("abc")  #the first characters are replaced by abc
print(f.read()) #prints from where the pointer is at start...ANT
f.close()

f=open("demo.txt","w+") #truncates ie wipes everything out
f.write("abc") #writes on the empty file

f=open("demo.txt","a+")
print(f.read())  #nothing in output
f.write("abc")  #adds text to end of string..pointer at end
f.close()

import os
os.remove("sample.txt")  #to delete a file