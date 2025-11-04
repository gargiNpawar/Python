name=input("Enter your name: ")
print("Welcome ", name , "to the adventure game!!")

answer=input("You are on a dirt road, you can go left or right to save yourself . which way would you choose?\n").lower()

if answer=="left":
    answer=input("You have reached a river shore , either you take a boat or swim across ?\n")
    if answer=="boat":
        print("You took the boat and you drowned due to cyclone")
    elif answer=="swim":
        print("You swam across and was eaten by an alligator")
    else:
        print("Not a VALID OPTION . You lose")

elif answer=="right":
    answer=input("You come a bridge, it it about to break , would you want cross it or head back ?\n")
    if answer=="back":
        print("You go back and lose")
    elif answer=="cross":
         answer=input("You cross the bridge and meet a stranger on the way, you decide whether you want to talk or not ?\n")
         if answer=="no":
             print("You lost a magical opportunity...You lose")
         elif answer=="yes":
             print("You talk to the stranger they give you gold , You WINNN!!!")  
         else:
             print("Not a VALID OPTION . You lose")    
    else:
        print("Not a VALID OPTION . You lose")

else:
    print("Not a VALID OPTION . You lose")
        
print("THANK YOU FOR PLAYING ",name)


    
