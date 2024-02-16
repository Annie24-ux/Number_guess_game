import random

min,max = 1,11
chosen_digit = random.randint(min, max)
chances = 11

def get_user_input():
    user_input = input("Guess a number from 1-10: ")
    return user_input

def checknum(user_input):
    num = int(user_input)
    if num < chosen_digit:
        print("Guess Higher")
    elif num > chosen_digit:
        print("Guess lower")
    elif num == chosen_digit:
        print("Congratulations, you got the number!"
              "The number was {num}")
        


def main():
    # get_user_input()

    input = get_user_input()
    checknum(input)


if __name__ == "__main__":
    main()