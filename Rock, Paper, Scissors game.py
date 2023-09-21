import random
l = ['rock', 'paper', 'scissors']

while True:
    user = input('Enter your choice rock, paper or scissors: ')

    com = random.choice(l)

    print("Your choice",user," computer choice",com)

    if user == com:
        print("Both players selected same. It's a tie!")
    elif user == "rock":
        if com == "scissors":
            print("You win! because Rock beats scissors.")
        else:
            print("You lose :paper beats rock!")
    elif user == "paper":
        if com == "rock":
            print("You win! because paper beats rock.")
        else:
            print("You lose :scissors beat paper!")
    elif user == "scissors":
        if com == "paper":
            print("You win! because scissors beat paper.")
        else:
            print("You lose :Rock beats scissors!")
            
    play_again = input('Play again? (y/n):')
    if (play_again == 'n'):
        break
