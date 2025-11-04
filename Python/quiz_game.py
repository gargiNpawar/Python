print("Lets play a game...Welcome to computer quiz")
playing=input("Do you want to play?")


if playing.lower() != "yes":
    quit()
print("OKay lets play")
score=0

answer=input("What is the capital of India?")
if (answer.lower()=="delhi"):
    print("correct")
    score += 1
else:
    print("U got the wrong answer")  

answer=input("Which is the largest mammal on earth?")
if (answer.lower()=="blue whale"):
    print("correct")
    score += 1
else:
    print("U got the wrong answer")

answer=input("which planet is called the red planet?")
if (answer.lower()=="mars"):
    print("correct")
    score += 1
else:
    print("U got the wrong answer")  

answer=input("which tallest mountain in the world?")
if (answer.lower()=="mount everest"):
    print("correct")
    score += 1
else:
    print("U got the wrong answer")  

answer=input("which is the first person to walk on the moon?")
if (answer.lower()=="neil armstrong"):
    print("correct")
    score += 1
else:
    print("U got the wrong answer") 

print("You got",str(score), "answers correct" )   
print("You got",str((score/5)*100),"%")  