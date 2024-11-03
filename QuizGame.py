ask = input("Do you want to play the Game?(Yes or No) ").lower()
score = 0

if ask == "yes":
    print("********************")
    print("Lets start the game!")
    print("********************")

    answer = input("What is the full form of CPU? ").lower()
    if answer == "central processing unit":
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong answer!")
        
    answer = input("What is the full form of GUI? ").lower()
    if answer == "graphical user interface":
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong answer!")
        
    answer = input("What is the full form of RAM? ").lower()
    if answer == "random access memory":
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong answer!")

    answer = input("What is the full form of ROM? ").lower()
    if answer == "read only memory":
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong answer!")

    answer = input("What is the full form of API? ").lower()
    if answer == "application programming interface":
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong answer!")
    
    print("****************")
    print(f"Your score = {score}")
    print("****************")

else:
    print("Ok, Have a good day!")

