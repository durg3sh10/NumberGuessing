import random

def guess ():
    random_no = random.randint(1,100)    # A random no. is generated by the program
    guess = 0

    while random_no != guess :
        guess = int(input("What is you're guess from 1 to 100 ?"))
        if guess == random_no :
            print("jackpot")
        elif guess < random_no  :
            print("you're guess is smaller")

        elif 100 >= guess > random_no  :
            print("you're guess is bigger")

        else :
            print("Oopss")


guess()




