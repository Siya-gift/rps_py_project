#rock paper scissors
import random



def game():
  while True:
      
    game_options = {'r':'⚫' , 'p':'📃' , 's':'✂'}
    computer_option = random.choice(list(game_options.keys()))
    user_input = input("Enter option ( r / p / s )? :").lower() 
      

    if user_input == computer_option:
        print(f"Both players selected {user_input.upper()}. It's a tie!")
    elif user_input == "r":
        if computer_option == "s":
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("***Rock smashes scissors! You win!***")
            print("*************************************")
            print()
        else:
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("Paper covers rock! You lose.")
            print("*************************************")
            print()
    elif user_input == "p":
        if computer_option == "r":
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("Paper covers rock! You win!")
            print("*************************************")
            print()
        else:
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("Scissors cuts paper! You lose.")
            print("*************************************")
            print()
    elif user_input == "s":
        if computer_option == "p":
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("Scissors cuts paper! You win!")
            print("*************************************")
            print()
        else:
            print()
            print("*************************************")
            print(f"***Computer's option: {computer_option.upper()} ************")
            print("Rock smashes scissors! You lose.")
            print("*************************************")
            print()
    else:
        print()
        print("*************************************")
        print(f"***Computer's option: {computer_option.upper()} ************")
        print("Invalid input! Please enter rock, paper, or scissors.")
        print("*************************************")
        print()
  
    print()
    print("**********************************************")
    play_again = input("Do you want to play again (y/n)? :").lower()
    print()
    
    
    if play_again == "n":
      break
    elif play_again == "y":
      continue
    else:
      print("Invalid Choice")
      break

game()