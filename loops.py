#------------------------------
# ABOUT PYTHON DICTIONARIES
#------------------------------

# A dictionary is a set of key-value pairs
    # Each value has a label called a key
    # Dictionaries ARE NOT sequences (not ordered)
    # They're indexed by their keys (not numbers)
    # (AKA "associative arrays" or "associative memories" in other programming languages)
    # They're the earliest stepping stone in thinking about "object-oriented programming"
    # (a design patter that revolves around modeling reusable objects in your code)

# Storing key value pairs in a dictionary allows you to group related data together
    # syntax = {key: value, key: value, key: value}
    # Key order doesn't matter, but they must be unique
    # If you add a duplicate key the original value associated with that key will be forgotten
    # Keys can be any immutable type, even tuples (but only if the items in the tuple are immutable)
    # Note, if you attempt to access a value without an existing key you will get an 'error'

#<hr>
print('-' *30)

#------------------------------
# MANIPULATE DICTIONARIES
#------------------------------

course = ['Ashley', 'Introducing Dictionaries', 'Beginner']
course = {'teacher': 'Ashley', 'title': 'Introducing Dictionaries', 'level': 'Beginner'}

# Access an individual value from the dictionary
# ('teacher' is the key, thus the value will be printed)

# Print the value paired to the key 'teacher'
print(course['teacher'])
print()

#----- METHODS -----

print('Access Dictionary Data:')

# Get a list of all the keys in a dictionary
print(course.keys())
# Get a list of all the values in a dictionary
print(course.values())
print()

#----- SORT IN LEXIGRAPHICAL ORDER -----

print('Sorted Dictionary Data:')
print(sorted(course.keys()))
print(sorted(course.values()))

# <hr>
print('\n' + ('-' *30))

#------------------------------
# UPDATE / ADD (MUTATE)
#------------------------------

course = {'teacher': 'Ashley', 'title': 'Introducing Dictionaries', 'level': 'Beginner'}

#----- UPDATE VALUES -----

# Change a paired value (connected to a key)
course['teacher'] = 'Jimbo'
print('Update Teacher Name:')
print(course.keys())
print(course.values())
print()

#----- ADD NEW -----

# Name of new key in square brackets
    # If Python can't find a matching key to update,
    # it will create a new key value pair inside the dicitonary
course['stages'] = 2
print("Add New Data:")
print(course.keys())
print(course.values())

#<hr>
print('\n' + ('-' *30))

#------------------------------
# DELETE AND EDITING
#------------------------------

#----- DELETE A PAIR -----
# Call the 'del' function, pass the value as an argument
del(course['stages'])
print(course.keys())
print(course.values())
print()

#----- RENAME A KEY (POP) -----

# Change a key
    # Remove and replace
        # (adds to the end of the dictionary)
        # (which doesn't really matter)
    # Syntax:
        # dic['new_key_name'] = dic.pop('existing_key_name)
course['Mentor'] = course.pop('teacher')
print("Use Pop:")
print(course.keys())
print(course.values())

#<hr>
print('\n' + ('-' *30))

#------------------------------
# ITERATE OVER DICTIONARIES
#------------------------------











#------------------------------
# PACKING / UNPACKING (DICTIONARIES)
#------------------------------











#<hr>
print('\n' *2)