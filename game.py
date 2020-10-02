import random

while True:
    klist = ["Rock","rock","Paper","paper","Scissor","scissor"]
    user = input("Welcome, please choose an option :").capitalize()
    if user in klist:
        pass
    else:
        print("You have written a wrong input ")
        continue
    comp = random.choice(klist)
    
    print(f"You choose {user}")
    print(f"Computer choose {comp}")
    
    if user == "Rock" and comp == "Scissor":
        print("You Won!")
    elif user == "Rock" and comp == "Paper":
        print("Compurt Wins!")
    elif user == "Rock" and comp == "Rock":
        print("It's a TIE! please try again:")
    
    elif user == "Paper" and comp == "Scissor":
        print("Computer Wins!")
    elif user == "Paper" and comp == "Paper":
        print("It's a TIE! please try again:")
    elif user == "Paper" and comp == "Rock":
        print("You Won!")
        
    elif user == "Scissor" and comp == "Scissor":
        print("It's a TIE! please try again:")
    elif user == "Scissor" and comp == "Paper":
        print("You Won!")
    elif user == "Scissor" and comp == "Rock":
        print("Computer Wins")
        
    repeat = input("Do you want to continue ?(Y/N)\n").capitalize()
    if "Y" in repeat:
        continue
    else:
        exit()
