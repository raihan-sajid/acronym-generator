# This is a simple acronym generator


# Get user input
user_input = input("Please enter the phrase you'd like made into an acronym: "+ "\n")

# Split the string into a list
phrase = user_input.split()

# Empty string to manipulate
acronym = ""

# OPTIONAL CODE TO OMIT PREPOSITIONS

# list of words that are omitted
omit_list = ['to','of','a','and','as','by','in']

# update phrase to remove omitted words
updated_phrase =[word for word in phrase if word.lower() not in omit_list]

#update2 = ''.join(update) - to test/print results

# loop through phase - comment these two lines out if NOT using omit_list
# for first in updated_phrase:
#     acronym = acronym + first[0].upper()


# loop through the phrase - comment these two lines out if using omit_list
for first in phrase:
    acronym = acronym + first[0].upper()

# print out the result
print(f'Acronym of {user_input} is {acronym}')
