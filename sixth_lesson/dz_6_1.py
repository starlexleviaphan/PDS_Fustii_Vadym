import random

n = random.randrange(1, 100)                              # Generate random number
t = int(6) # amount of tryings
print("Guess the number, Neo :)")                         # Greetings
print("You have", t, "attempts")

for i in range(t + 1):
    if i == t:                                            # Check if you out of attempts
        print("You've failed :(")
        break
    else:
        inp = int(input("Enter your number: "))           # Enter number by user
        if inp == n:                                      # Checking is entered number is correct
            print("You win!!!")
            print("Number of tryings = ", i + 1)
            break
        elif inp < n:                                     # Checking is entered number is lover then correct
            print("entered number is lower then desired")
        elif inp > n:                                     # Checking is entered number is higher then correct
            print("entered number is higher then desired")
