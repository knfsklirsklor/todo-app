# import webbrowser
#
# user_term = input("enter a search term: ").replace(' ', "+")
#
# webbrowser.open("https://www.google.com/search?q=" + user_term)

# import shutil
#
# shutil.make_archive("output", 'zip', 'files')

from parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10): ")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(parse(user_input))
print(rand)