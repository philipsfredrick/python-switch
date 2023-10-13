# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ______"
youtuber = "Nonso"

# few ways to do this: +, .format function, f"" string.
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# madlibs = f"Computer programming is {adj}! It makes me so excited all the time because \
# I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"


# def my_function_with_args(username, greeting):
#     print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
# my_function_with_args("nonso", "hello")


# youtube = "social platform"
# print("Click button to subscribe to " + youtube)
# print("Click button to subscribe to {}".format(youtube))
# print(f"Click to subscribe to {youtube}")

madlibs = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlibs)
