with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O\n")
    f.write("using java.\nI like programming\n")

with open("practice.txt","r") as f:
    data=f.read()    
new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f: #overwrite happens
    f.write(new_data)

def  check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word) != -1):  #else we write- "word in data"
            print("FOUND")
        else:
            print("NOT FOUND")    
check_for_word()

def check_for_line():
    word="like"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                #if we don't write return they check for the rest of lines as well
            line_no+=1
    return -1 #if no word in text        
check_for_line()

with open("practice2.txt","r") as f:  #nos in text are sub strings 
    data=f.read()
    print(data)

    num="" #intialize with empty string ; num collects digits until comma
    for i in range(len(data)):
        if(data[i]==","):
              if (num != ""): #prevents the error of converting an empty string to int
                if (int(num)%2==0):
                  print(int(num))
                num=""
        else:
            num+=data[i]    

                    #OR
count=0                    
with open("practice2.txt","r") as f:
    data=f.read()
    nums=data.split(",")   #nums gives us a list['1','2','43','54','76','84','90','101','43']...where each no is a substring
    for val in nums:
        if(int(val)%2==0):
            print(int(val))
            count+=1 
print("NO OF EVEN NOS:",count)  #not in loop

