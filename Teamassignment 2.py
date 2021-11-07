import random

num = random.randrange(1, 11)
print(num)

# take off when turn in

guess = int(input("please choose a number from 1 and 10 ="))

while guess != num:
    if guess > num:
        print("Please choose lower")
    elif guess < num:
        print("Please choose higher")
    else:

        break

    guess = int(input("Please choose a number 1 and 10 ="))

print("Correct!")