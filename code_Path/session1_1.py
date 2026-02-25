'''
problem:1
Hundred Acre Wood
UPI plan
Function that prints strings 

'''
def welcome():
    print("Welcome to the Hundred Acre Wood!")
welcome()

"""
Problem:2
Accepts single parameter (name)
prints 

declare the function
use print with fname

"""
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
greeting("Michael")

"""Problem: 3
Function that prints catchprahse 
Accepts a character  as parameter
prints
Declare the function 
compare the character  using if statements

"""
def print_catchphrase(character):

    #if stament to compare the catchphrase

    if character == "Pooh":
        print("Oh bother!")

    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")

    elif character =="Eeyore":
        print("Thanks for noticing me.")

    elif  character == "Christopher Robin":
        print("Silly old bear.")

    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

'Testing'

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)


"""  
Problem: 4
Aceepts 0-indexed list, non-negative integer
returns element
if x not valid return 'none'
Implement:
edge case 


"""
def get_item(items, x):
    #edge case
    if x <0 or len(items)< x :        
        return None
    
    return print(items[x])
    




'Testing'



items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))

'''
Problem:5 
Accepts list of integers
retuns the sum 
Implement:
edge case
variable to store total
Use for loop to iterate over the list


'''
def sum_honey(hunny_jars):
    sum = 0

    #edge case
    if not hunny_jars:
        return 0
    
    #iterate over the list
    for x in hunny_jars:
        sum += x
    return print(sum)


hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

"""
Problem: 6
Accepts list of integers
multiply  integers by 2
returns the new list

implement:
loop to iterate over the list
multiply by 2
 append the list to the new list

"""

def doubled(hunny_jars):
    new_list= []
    if not hunny_jars:
        return []

    for x in hunny_jars:
        new_list.append(x*2)
    return new_list

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

"""
problem 7
Accepts list of integers 
find the thereshold value
loop to iterate over the list
compare the value to the threshold value
return the value that are less than the threshold value

Implement:
edge case: Empty list
variable to store the new list
iterate over the list
compare the value to the threshold value



"""
def count_less_than(race_times, threshold):

    newlist= []
    #edge case
    
    
    for x in race_times:
        if x < threshold:
            newlist.append(x)
    return len(newlist)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

"""

"""