import random
import colorama
from colorama import Fore
colorama.init(autoreset=False)

def start_game():
    while True:
        name = input("Enter name: ")
        if name.isalpha():
            break
        else:
            print("Only letters are allowed here")

    guess_number(name)

def guess_number(player_name):
    correct_number = random.randint(1, 10)
    attempts = 3 

    while attempts > 0:
        try:
            guess = int(input(f"{Fore.RESET}Hey {Fore.CYAN}{player_name}{Fore.RESET}, guess the correct number from 1 to 10! You have {Fore.GREEN}{attempts}{Fore.RESET} tries left! Your guess: "))

            if 1 <= guess <= 10:
                if guess == correct_number:
                    print(f"{Fore.MAGENTA}Congratulations! You guessed the correct number!")
                    break
                else:
                    print(f"{Fore.RED}Incorrect guess. You have {attempts - 1} tries left.")
                    attempts -= 1
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.")

    print(f"{Fore.RED}The correct number was {correct_number}. Game over!")

if __name__ == "__main__":
    start_game()
    input("Press Enter to exit...")