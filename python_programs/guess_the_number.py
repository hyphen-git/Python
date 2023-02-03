import random

bot_num = random.randint(1, 100)
user_num = None
count = 0

while (user_num != bot_num):

    user_num = int(input("Enter your guess : "))
    count = count+1
    if (user_num > bot_num):
        print("try smaller number")
    elif (user_num < bot_num):
        print("try greater number")
    else:
        print("You Guessed it right!")
        print(f"you guess it in a {count} attempts")
        break
