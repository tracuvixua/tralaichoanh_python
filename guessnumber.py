import random
a = random = random.randint(1, 50)
print(a)
guess = int(input("you have only 5 chances, guess a number between 1 and 50: "))
i = 0
while guess != a:
    if i == 5:
        print("you lost")
        break
    elif guess > a:
        print("too high")
        i = i + 1
        print ("You have", 5 - i, "chances left")
    elif guess < a:
        print("too low")
        i = i + 1
        print ("You have", 5 - i, "chances left")
    guess = int(input("guess again: "))
else:
    print("you got it")