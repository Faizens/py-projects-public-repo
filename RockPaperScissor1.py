import random 

emojis = {'r':'⬛','s':'✂','p':'🧻'}
moves = ['r', 'p', 's']

while True:
        user_choice = input("Enter 'Rock/Paper/Scissor' 'r/p/s': ").lower()
        if user_choice not in moves:
                print("Invalid choice! Try again")
                continue
        
        computer_choice = random.choice(moves)

        print(f"player chosed: {emojis[user_choice]}")
        print(f"computer chosed: {emojis[computer_choice]}")
        
        if user_choice == computer_choice:
                print("Tie")
        elif \
        (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "s" and computer_choice == "p") or \
        (user_choice == "s" and computer_choice == "p") :
                print("You won")
        else:
                print("You Lose")      
                
        play_again = input("Continue? (y/n): ").lower()
        if not play_again == "y":
                print("Thanks for playing")
                break 
        else:
                continue


        
