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

print("ITERATE OVER DICTIONARIES:\n")

vid_games = {'Halo': 3.5, 'Call of Duty': 4.5, 'Assasins Creed': 5.0}

#----- FOR LOOP (INEFFICIENT) -----

# This will give us all the keys ...
for item in vid_games:
    print(item)
print()

# This will give us all the values ...
for item in vid_games:
    print(vid_games[item])

#<hr>
print('\n' + ('-' *30))

#----- THE ITEMS() METHOD -----

# The 'items()' method returns a list of tuples (when called on a dictionary)
    # Each tuple contains a key and value for every item in the dictionary
    # Note, the method loops over a list of tuples representing the dictionaries keys and values
    # (instead of iterating directly over the dictionary)

print("Call 'list.items()' method on dictionary:")
print(vid_games.items(), '\n')

# Print out each tuple in course.items()
for item in vid_games.items():
    print(item)
print()

#----- USE MULTIPLE ASSIGNMENT -----

# Access the key and value separate from one another ...
for key, value in vid_games.items():
    print(key, 'was rated', value, '/ 10')

#<hr>
print('\n' + ('-' *30))

#------------------------------
# PACKING VARIABLE ARGUMENTS
#------------------------------

# Add "a series of variable arguments" into a signle dictionary
    # Each variable name becomes a key
    # Each variable reference becomes a corresponding value

# Compare:
    # When packing with python sequences
    # We pass multiple positional arguments
    # and capture them into a tuple

# Compare:
    # When packing with python dictionaries
    # We pass multiple variable arguments
    # and capture them into a dictioary

# What's a variable argument?
    # When we call functions we usually pass positional arguments
    # (comma separated values received by the function in the order wich they're sent)
    # The key difference between variable arguments and poisitonal arguments is for
    # for variable arguments the order doesn't matter. AND, unlike positional arguments they're named

#----- CREATE A SIMPLE FUNCTION -----

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

#----- USE POSITIONAL ARGUMENTS -----

print_teacher('Ashley', 'Instructor', 'Python')
print()

#----- USE VARIABLE ARGUMENTS -----

# Problem:
    # If our function call is not placed close to its function definition
    # it becomes less obvious what the positional arguments are for
    # (hard to remember and for others to understand)

# Resolution:
    # Add clarity to your code by using variable arguments
    # (also referred to as "keyword arguements" or "named arguments")

# Variable names have to mach the parameter names in our definition
    # This is how Python matches arguments and parameters when the order doesn't matter
    # To convert the positional arguments to variable arguments,
    # simply make them look like variable assignements
    # (variable names HAVE TO MATCH the parameter names in the function definition)

print_teacher(name='Ashley', job='Instructor', topic='Python')

#<hr>
print('\n' + ('-' *30))

#------------------------------
# UNKNOWN VARIABLE ARGUMENTS
#------------------------------

#----- PASS UNKNOWN VARIABLE ARGUMENTS -----

###### 4:20

###### WHY????

# "So, just like when our code can call for passing an unknown or arbitrary number
# of positional arguments to a function, it might also call for passing an unknown
# or arbitrary number of variable arguments to a functin.""












    











#<hr>
print('\n')
