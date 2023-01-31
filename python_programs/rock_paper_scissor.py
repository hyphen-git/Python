import random

def bot_play():
    bot_in = random.randint(0 ,2)
    if(bot_in == 0):
        return "rock"
    elif(bot_in == 1):
        return "paper"
    elif(bot_in == 2):
        return "scissor"
    else:
        return "none selected"

bot_move = bot_play()


user_move = input("Please enter rock , paper or scissor : ") 


if(user_move == bot_move):
    print("Its a Draw\n", "YOU : " , user_move , "\nBOT : " , bot_move)
elif(user_move == "rock" and bot_move == "paper"):
    print("BOT won.\n", "YOU : ", user_move , "\nBOT : " ,bot_move)
elif(user_move == "rock" and bot_move == "scissor"):
    print("YOU won.\n", "YOU : ", user_move , "\nBOT : " , bot_move)
elif(user_move == "paper" and bot_move == "rock"):
    print("YOU won.\n", "YOU : " ,user_move , "\nBOT : " , bot_move)
elif(user_move == "paper" and bot_move == "scissor"):
    print("BOT won.\n", "YOU : " , user_move , "\nBOT : " , bot_move)
elif(user_move == "scissor" and bot_move == "rock"):
    print("BOT won.\n" , "YOU : " , user_move , "\nBOT : " , bot_move)
elif(user_move == "scissor" and bot_move == "paper"):
    print("YOU won.\n" , "YOU : " , user_move , "\nBOT : " , bot_move)







