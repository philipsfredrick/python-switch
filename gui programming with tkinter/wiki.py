# pip install wikipedia

# importing the module
import wikipedia

# finding result for the search
# sentences = 2 refers to number of line
# result = wikipedia.summary("Nigeria", sentences = 5)
result = wikipedia.summary("Interswitch", sentences = 5)

# printing result
print(result)