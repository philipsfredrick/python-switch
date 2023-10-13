import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry, guess again. Too low.")
#         elif guess > random_number:
#             print("Sorry, guess again too high.")
#     print(f"Yay, congrats. You have guessed the number {random_number} correctly.")
# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high as low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess} correctly!")

computer_guess(1000)



# data = ("John", "Doe", 53.44)
# format_string = "Hello"
# print("%s" + "%s %s. Your current balance is %.2f" % (format_string, data))

# astrings = "Hello world!"
# print(astrings.index("o"))
# print(astrings.count("l"))
# print(astrings.upper())
# print(astrings.lower())
# print(astrings[3:7])
# print(astrings[::-5])
# print(astrings[:5])
# print(astrings[5:])
# print(astrings[::-1])

# den = float(7)
# print(den)
# den = 8.0
# print(den)
# print(type(den))

# statement = False
# another_statement = True

# if statement is True:
#     pass
# elif another_statement is True:
#     pass
# else:
#     pass

# x = 2
# if x == 2:
#     print("x equals two!")
# else:
#     print("x does not equal to two.")
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# numbers = []
# strings = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# strings.append("hello")
# strings.append("world")
# strings.append("care")
# print(numbers)
# print(strings)
# number = 1 + 2 * 3 / 4.0
# print(number)

# remainder = 11 % 3
# print(remainder)

# combe = numbers + strings
# print(combe)
# print(numbers * 3)

# x_list = ["x", 1,2,3]
# print(x_list)
# print("My list is %s: " % x_list)

# data = ("Jane", "Doe", 49.999)
# result_string = "Hello %s %s. Your current balance is $%.2f"
# print(result_string % data)

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%s."

# print(format_string % data)

# print(len("hello worlds"))

# print(result_string.index("b"))

# astring = "Hello world!"
# afewwords = astring.split()
# print(afewwords)
# for x in afewwords:
#     print(x)
# for y in astring:
#     print(y)