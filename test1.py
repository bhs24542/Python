'''Docstring this is a program to check if a person can vote in NZ or not
By Jervis Xu on 11-05-26'''

is_resident = False
#ask the user's name
name = input("What is your name?\n")
while True:
    try:
        #ask the user his age
        age = int(input("How old are you?\n"))
        break
    except:
        print("That is not a number\n")
#end of while loop

#ask if he is a resident
while True:
    resident = input("Are you a resident? Y/N\n")
    if resident.lower() == "y":
        is_resident = True
        break
    elif resident.lower() == "n":
        is_resident = False
        break
    else:
        print("please type in either Y or N")
#evaluate if the person can vote
if age > 17 and is_resident:
    print("You can vote\n")
else:
    print("You can not vote\n") 
in ChildProcessError