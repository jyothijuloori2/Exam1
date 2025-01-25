import random
def guess_number():
    secret_num=random.randint(1,100)
    attempts=0
    print("try to guess a number between 1 and 100")
    while True:
        try:
            guess=int(input())
            attempts+=1
            if guess < secret_num:
                print("Too Low! Try again.")
            elif guess > secret_num:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {secret_num} in {attempts} attempts.")
                break  # Exit the loop when the correct guess is made
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
def main():
    guess_number()
main()