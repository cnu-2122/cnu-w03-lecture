# Week 2 review

# Lists

a = [5, 2, 4.4, 'bonjour!']
# print(len(a))

# b = a
b = a.copy()
# b = copy(a)
# print(b)

# Change one element in b
b[1] = 10
print(b)
print(a)
# Lists are mutable.

# # With numbers...
# x = 1
# y = x
# x = 2
# print(y)

# List methods
b.append(0)
# print(b)

# b.append(1, 2, 3)    # doesn't work!
# b.append([1, 2, 3])
# b.extend([1, 2, 3])
b.extend([0] * 3)     # [0, 0, 0]
print(b)

print(b.count(0))

# Get some help!
# help(list.append)
# help(print)


# Functions: return and print()
def greet(name):
    output = 'Hello, ' + name + '! :)'
    return output
    # print(output)
    # return None

greeting_message = greet('Charlotte')
print(greeting_message + ' How are you doing this fine morning?')


# Slicing and indexing

def every_mth_character(my_string, m):
    '''
    Returns a string of every mth character in my_string.
    '''
    # With a loop
    output = ''
    # counter = 0
    for counter, char in enumerate(my_string):
        if counter % m == 0:
            output += char
        # counter += 1
    return output

def every_mth_character(my_string, m):
    '''
    Returns a string of every mth character in my_string.
    '''
    return my_string[::m]
    # output = my_string[::m]
    # return output
    

print(every_mth_character('Python is great!', 2))