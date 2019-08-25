# The Complete Guide to Mastering Python 3

# Lessons:

# 1: Python Fundamentals (DONE)
# 2: Data Structures     (DONE)
# 3: Lists               (DONE)
# 4: Dictionaries        (DONE)
# 5: Sorting 
# 6: Searching   
# 7: Functions 
# 8: Classes
# 9: Input/Output Operations         
#10: Trees
#11: Object Oriented Programming (OOP)
#12: Hash Tables
#13: Big-O Notation
#14: Structured Techniques
#15: Functional Techniques
#16: Github's mtdvio's "Every Programmer Should Know"
     # https://github.com/mtdvio/every-programmer-should-know
#17: Methods

## Resources:
     # Best Python Tutorials: https://ducards.com/lists/WZ3Yw
     # Reddit Learn python: https://www.reddit.com/r/learnpython/wiki/index
     # Automate the Boring Stuff: https://automatetheboringstuff.com/
     # Google Python Course: https://developers.google.com/edu/python/
     # w3schools.com https://www.w3schools.com/python/default.asp
     # Python Official Documentation: https://docs.python.org/3/tutorial/

##################################################################
##################################################################
# 1: Python Fundamentals #########################################
# 2: Data Structures #############################################
# 3: Lists #######################################################
##################################################################
##################################################################

#!/bin/python3

#printing
print("Hello, World!")
#or
my_string = "Hello, World!"
print(my_string)

#to get input from user: (std in)
N = int(input())
#gets input and converts it into int. if not int it throws an error
print(type(N)) #prints out the type of N
print(N)

#if statements:
if N > 10:
    print("N is greater than 10")
elif N < 10:
    print("N is less than 10")
else:
    print("potato")

#one line if and else statement
print("A") if N > 1 else print("B")

#one line if statement
if N > 2: print("N is greater than 2")

#one line if with 2 else
print("A") if N > 3 else print("=") if N == 3 else print("B")

# you can use and / or as words to do conditionals
"""
this is a multiple comment thing
"""

# range(5) creates a list from 0 to 5
for i in range(5):
    print(i)

#HackerRank coding challenge
N = int(input())
if (N >= 1) and (N <= 100): #check the range if between 1 and 100
    if (N%2 == 1) or (((N >= 6) and (N <= 20))): #odd or in range
        print("Weird")
    else:
        print("Not Weird") #otherwise it's even and out of range

# Variables are created when avalue is assigned to it. No int/str/etc...
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z =  x + y
print(z)
# integer Division is //
# actual float division is /

# integer is whole number. Can be positive or negative
# Float is any number (+ve or -ve) that contains 1 or more decimals
# complex numbers contain the float and floatj. e.g: (25 + 3j)
# For floats, j is the imaginary part

# doing int(2.8) will round down to 2. int() always rounds down.
# int() can convery anything, even string if string is an integer.
# str() converts anything to string.
# in python, " and ' are the same.

# a string in python is an array of bytes. each letter takes one spot.
a = "potato "
print(a[0]) # this will print p
print(a[0:4]) # this will print "potat"

print(a.strip()) # strip removes white space from the beginning or the end
print(len(a)) # will print 7, which is the array length of a.
print(a.lower()) # will print the string in lower case
print(a.upper()) # will print the string in upper case
print(a.replace("t", "p")) # will replace all the t with p
print(a.split("t")) #will return "po" and "a" and "o"
# in python, ** is the power.
# % is the Modulus (or remainder term)
# you can do, +=, -=, *=, /=, %=, //=, **=,  (>=) and (<=)
# logical operators: and, or, not
# is and is not are used to compare if something is the same object!!!!
# not the same value, just the same object type. e.g: x is y (true if both ints)
# in and not in, checks to see if x in y: if x's value is present in y.

# RANDOM INFO - FROM GOOGLE PYTHON TUTORIAL:
# import modules used here -- sys is a very standard one
# import sys

# Gather our code in a main() function
def main():
    print 'Hello there', sys.argv[1]
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result
# Now can refer to sys.xxx facilities
sys.exit(0) #exits the application

s[1:4] is 'ell'
# %d int, %s string, %f/%g floating point

a = [5, 2, 3, 1, 4]
b = a.sorted() ##### THIS DOES NOT CHANGE THE ORIGINAL LIST
print b

# CAPITAL letters are smaller than lowercase so they get sorted first

strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len)
## yoru output is ['d', 'bb', 'ccc', 'aaaa']

# the sort() function changes the actual one while sorted returns a sorted
# list and doesnt change the original list.


'''
To create a size-1 tuple, the lone element must be followed by a comma.

  tuple = ('hi',)   ## size-1 tuple
It's a funny case in the syntax, but the comma is necessary
to distinguish the tuple from the ordinary case of putting an expression
in parentheses. In some cases you can omit the parenthesis and Python will
see from the commas that you intend a tuple.
'''

nums = [1, 2, 3, 4]

squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
strs = ['hello', 'and', 'goodbye']

shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANANA']


#-- chars starting at index 1 and extending up to but not including index 4

# (==) (!=) (>=) (<=)if,elif, else

print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")

i = 1
while i < 6:
    print(i)
    i += 1
    break
# the break statement breaks out of the while loop
i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue # this way the while loop goes back to continue and skips the rest
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) # this will print the items in the list

for x in "banana":
    print(x) # this will print the letters in banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue #skips the printing and continues the loop
    print(x)


for x in range(6): #prints 0 to 5 (6 numbers starting from 0)
    print(x)

for x in range(2, 6): #prints  2,3,4,5 (SKIPS 6!!!)
    print(x)

for x in range(2, 30, 3): #starts from 2 - 29, +3 with each increment
    print(x)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") #this will print I am from Sweden
my_function("India") # ... from india.
my_function() #NOTE: This will use the default value of Norway.
my_function("Brazil") #... from Brazil.

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

x = lambda a : a + 10
print(x(5))
#lambda function can only have one expression.
#lambda function can take in any numberof arguments.
x = lambda a, b : a * b
print(x(5, 6))
cars.append("Honda") #adds an element to the array.
cars.pop(1) #deletes the second element of the array.
cars.remove("Volvo") #removes the FIRST occurance of VOlvo.
fruits.insert(1, "orange") #inserts at the specified index.


# 3: Lists #######################################################

'''
List is a collection which is ordered and changeable.
Allows duplicate members.

Tuple is a collection which is ordered and unchangeable.
Allows duplicate members.

Set is a collection which is unordered and unindexed. No duplicate members.

Dictionary is a collection which is unordered, changeable and indexed.
No duplicate members.
'''
#example:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[2] = thislist[0]
print(thislist[0][1]) #will print p
# you can loop through the list
for x in thislist:
    print(x[0])

# you can use "in" to check if something exists in a list:
if "apple" in thislist:
    print("damn")
    len(thislist) #will print the number of items in thislist
# to add items to a list do list.append("object")
thislist.append("Clamentine")
print(thislist)

# to add an item at a specific location do insert
thislist.insert(1, "Orange")
print(thislist) # now orange will be in index 1 instead of the end

thislist.remove("Orange") # will remove the first occurance of orange from the list

thislist.pop() # will remove the last item of the list OR YOU CAN DO:
thislist.pop(1) # this will remove banana
print(thislist)
del thislist[0] #using del deletes a specified index.
del thislist # this deletes the entire list completely.

thislist = ["apple", "banana", "cherry"]
thislist.clear() # empties the list
# you can also use the list constructor to make a list.
thislist = list(("apple","banana","Strawberry"))
list2 = thislist.copy() # copies the list
x = thislist.count("apple") # returns the number of apple present in this list
x = thislist.index("apple") # returns the index of the first element to be apple

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)   # this will add cars to the end of fruits.
# for extending lists, you can add different types. one can be string one can be int
fruits.reverse() #will reverse the current order of the list

fruits.sort() # this will sort the list
# sort can list a list alphabetically.
# sort lists a list ascending by default.

# you can also determine the sorting criteria
# list.sort(reverse=True|False, key=myFunc)
# reverse = True will sort the list in Descending order instead
# key = myFunc will use a function to specify the sorting criteria

# A function that returns the length of the value:
def myFunc(e):
  return len(e)



cars = ['Ford', 'Mitsubishi', 'BMW', 'VW'] #this is a list with square brackets

cars.sort(key=myFunc) #the key, which is the length value, will sort this
# this will sort this from smallest length to largest length

for item in cars:
    print(myFunc(item))
    
cars.sort(reverse=True,key=myFunc) #this will sort it from largest length first
for item in cars:
    print(myFunc(item))

'''
Without using loops: * symbol is use to print the list elements in a
single line with space. To print all elements in new lines or separated
by space use sep=”\n” or sep=”, ” respectively.
'''
# Python program to print list 
# without using loop 
  
a = [1, 2, 3, 4, 5] 
  
# printing the list using * operator separated  
# by space  
print(*a) 
  
# printing the list using * and sep operator 
print("printing lists separated by commas") 
  
print(*a, sep = ", ")  
  
# print in new line 
print("printing lists in new line") 
  
print(*a, sep = "\n")

#printing the 123...N without spaces in between. print takes a lot of 
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(i+1)
    print(*arr, sep='')

# sorting a list of dictionaries
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
def myFunc2(e):
  return e['year']

cars.sort(key=myFunc2)
print(cars)
# this sorted our dictionary based on the year in Ascending order. smallest to biggest

# Tuples are ordered but UNCHANGEABLE!!!!. Tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


if "apple" in thistuple: #check to see if apple is in thistuple
    print("yay")

#you can create a tuple by doing tuple(("a","b","c")) this will create a tuple

# set is unordered and unindexed.
# a set is never in the same order. printing it, you can see that the order changes
# with every print.

thisset = {"apple", "banana", "cherry"} #a set is created with curly brackets
# NOTE: THERE ARE NO INDEXING IN A SET!!!
# YOU CANNOT CHANGE ITEMS IN A SET BUT YOU CAN ADD ITEMS!!!

thisset.add("orange") # you can do this to add to the set
thisset.update(["orange", "mango", "grapes"]) # you can add multiple items

# thisset.remove() or thisset.discard() will remove the item for you
# EVERY ELEMENT IN THE SET IS UNIQUE! YOU CANNOT HAVE REPEATING VALUES!!!!!!!!
# using del completely removes the item from the memory. calling it will get an error
# END ########################################################################

###################################################################################
# 4: DICTIONARIES #################################################################
###################################################################################

# Dictionary in python is stored by keys. There are no indexes.
# The dictionary is unordered. Changeable and indexed.
# but you cant index the key, you can index values belonging to the key.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys()) # in this case, all of, brand, model and year are keys

# to access an item in the dictionary: ["key"]. or ["key"]["value"]
x = thisdict["model"] # x will be the value associated with model in this case
x = thisdict.get("model") # this does the same thing as above.
thisdict["year"] = 2018 # this will change the value of year

# when you loop through a dictionary, it returns to you the keys.
for x in thisdict:
    print(x)

# to return the values instead of the keys, we do: thisdict.values()
for x in thisdict.values():
    prit(x)

# if you want to loop through both keys and values we can do it as well
for x,y in thisdict.items():
    print(x,y) # x will be the key, y will be the value associated with that key

if "model" in thisdict:
    print("k")

#len will give you the length of key-value pairs in the dictionary

# Adding a key and value to the dictionary is done by referencing a new key
# if you use an existing key, you will change it's value.

thisdict["color"] = "red" # you can add values  this way
thisdict.pop("model") # will remove the key and value item (both)
del thisdict["model"] # will remove. same as above.

thisdict.popitem() # in 3.7 and after, removes last inserted item.
# CAREFUL: Before 3.7, this would remove a random item.

del thisdict # you can use that to delete the dictionary completely. Deems it unusable
thisdict.clear() # clears the dictionary, you can still use it.

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# this constructs a dictionary for you.
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
thisdict.values() # returns all the values, without the keys

# use .copy() to create a copy of the dictionary

# END ########################################################################

###################################################################################
# 5: SORTING ######################################################################
###################################################################################

# Objective: Given a list of unsorted grades, sort them so that failing grades
# are at the front. Do not use a new Data Structure.

# Quick Sort: Complexity = nlogn, worst is n^2
'''
divide and conquer algorithm. We partition by selecting a pivot
All elements smaller than the pivot are moved to to the left, and all greater to right
Each sublist is recursively sorted as well.
In practice choosing a random pivot almost certainly yields O(n log n) performance.
'''



# Merge Sort: Complexity = nlogn, worst is nlogn
'''
An example of merge sort. First divide the list into the smallest unit (1 element),
then compare each element with the adjacent list to sort and merge the two adjacent
lists. Finally all the elements are sorted and merged.
'''



# Search (Requires list to be sorted)

# Merge (Requires list to be sorted)

# if you want to combine two lists.
# sorted(l1 + l2) this will return a sorted list of both concatenated
first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]
# One way:
resulting_list = list(first_list)
resulting_list.extend(x for x in second_list if x not in resulting_list)

# Another way:
in_first = set(first_list)
in_second = set(second_list)

in_second_but_not_in_first = in_second - in_first

result = first_list + list(in_second_but_not_in_first)
print result  # Prints [1, 2, 2, 5, 9, 7]

first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]
# One way:
resulting_list = list(first_list)
resulting_list.extend(x for x in second_list if x not in resulting_list)

# Another way:
in_first = set(first_list)
in_second = set(second_list)

in_second_but_not_in_first = in_second - in_first

result = first_list + list(in_second_but_not_in_first)
print (result)
# Prints [1, 2, 2, 5, 9, 7]
# this only gets rid of duplicates in another set

first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]

#The | will get rid of all the duplicates of the set.
resultList= list(set(first_list) | set(second_list))

print(resultList)
# Results in : resultList = [1,2,5,7,9]

# This will get rid of all duplicates



# INTERVIEW QUESTIONS:
'''
Senior Software Developer Interview Kitchener, ON

Given an array of int[] like 1,2,3
Find the next largest  integer than can be made with these digits (e.g.: 2,1,3)
'''

# Binary Search Tree:


# Heap VS Stack:
'''
Stack is used for static memory allocation and Heap
for dynamic memory allocation, both stored in the computer's RAM .

Variables allocated on the stack are stored directly
to the memory and access to this memory is very fast,
and it's allocation is dealt with when the program is
compiled. When a function or a method calls another
function which in turns calls another function etc., the
execution of all those functions remains suspended until
the very last function returns its value. The stack is always
reserved in a LIFO order, the most recently reserved block is
always the next block to be freed. This makes it really simple
to keep track of the stack, freeing a block from the stack is
nothing more than adjusting one pointer.

Variables allocated on the heap have their memory allocated at run
time and accessing this memory is a bit slower, but the heap size
is only limited by the size of virtual memory . Element of the heap
have no dependencies with each other and can always be accessed randomly
at any time. You can allocate a block at any time and free it at any time.
This makes it much more complex to keep track of which parts of the heap are
allocated or free at any given time.

You can use the stack if you know exactly how much data you need to
allocate before compile time and it is not too big.	You can
use heap if you don't know exactly how much data you will need at
runtime or if you need to allocate a lot of data.

In a multi-threaded situation each thread will have its own
completely independent stack but they will share the heap.
Stack is thread specific and Heap is application specific.
The stack is important to consider in exception handling and
thread executions.


'''

# Stack issues:

# Ranking Based on Marks:

# Braces/Stacks

# Algorithms

# O(n) solution for repeated values in a list: (Other solutions
# are worst case scenario n^2
'''
Have another array, and as you go through that array
if the array is empty, add it to that location
otherwise, compare and if it's the same, then that is one
of the repeated numbers.
'''
# this will take a list and will stop when 2 repeated values occur
def find_repeating(lst, count=2):
    ret = []
    counts = [None] * len(lst)
    for i in lst:
        if counts[i] is None:
            counts[i] = i
        elif i == counts[i]:
            ret += [i]
            if len(ret) == count:
                return ret
                


# given two string arrays arr1 and arr2 for example,
# return the percentage of strings in arr1 that appear in arr2

# Selecting the element that was repeated in every array from a set of arrays

'''
write for us an application that will take any sequence of 5 numbers,
and write out its digits in order from low to high, eg,
given "85967" your output should be "56789." Do this in five minute.
'''

'''
Given an array, write a function to output the ranking of each
value in the array. Equal values should have the same ranking.
For example: input of [25, 7, 54, 90, 7] should result in [2, 1, 3, 4, 1]
'''

# SYNTAX AND LOGIC ERRORS IN C#
# TRY CATCH EXCEPTIONS
# PUBLIC AND PRIVATE VARIABLES
# STATE ERRORS OR OPTIMIZATIONS FOR C# CODE


'''
Given an array of arrays where each sub-array contains an arbitrary number of
random strings, find the strings that occur in every sub-array and return them
(the returned result strings must also be in an array). There can be duplicates
of the same string in any of the sub-arrays.
'''

# ABSTRACT VS INTERFACE

# Algorithm: 2 arrays of names, merge…

# OBJECT ORIENTED PROGRAMMING:

# WHAT IS REFLECTION?

# WHAT IS HASH?

# HOW WOULD YOU MERGE TWO ARRAYS OF NAMES?



###################################################################################
# 8: CLASSES ######################################################################
###################################################################################

#this is a class with a property x.
class MyClass:
  x = 5
  
p1 = MyClass()
print(p1.x) #this will print 5.

# THE INIT FUNCTION!!!
# built-in __init__() function.
'''
All classes have a function called __init__(),
which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Objects can also contain methods.
# Methods in objects are functions that belongs to the object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# The self parameter is a reference to the class instance itself,
# and is used to access variables that belongs to the class.

'''
The self parameter is a reference to the class itself,
and is used to access variables that belongs to the class.

It does not have to be named self ,
you can call it whatever you like, but it has to be
the first parameter of any function in the class:
'''
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc): #this works, because it is the first item defined.
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40 # this is how you modify properties of the class
del p1.age # this deletes the property.
del p1 # this deletes the entire object of the class.

'''
Inheritance allows us to define a class that inherits all the methods
and properties from another class.

Parent class is the class being inherited from,
also called base class.

Child class is the class that inherits from
another class, also called derived class.
'''

# Any class can be a parent class, so the syntax is the
# same as creating any other class:

# create another class that takes the first class.
# Use the pass keyword when you do not want to add
# any other properties or methods to the class.


class Student(Person):
    pass

# When you add the __init__() funcion, the child class will no longer
# inherit the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function,
# add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.graduationyear = 2019 #now this class has the parents properties and its own new one as well

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year #this should be a variable call.

x = Student("Mike", "Olsen", 2019)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# An iterator is an object that you can count and iterate through.
#The __iter__() method acts similar, you can do operations
# (initializing etc.), but must always return the iterator object itself.

#The __next__() method also allows you to do operations,
# and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self): #has to always take self, can take other stuff as well.
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else:
      raise StopIteration #this prevents the iteration from continuing forever
    
myclass = MyNumbers()
myiter = iter(myclass)

'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code,
regardless of the result of the try- and except blocks.
'''

try:
  print(x)
except: #when an error is raised, instead of crashing, it does this for you instead.
  print("An exception occurred")

try:
  print(x)
except NameError: #if a name error occurs, will call this block of code
  print("Variable x is not defined")
except:           # this is for all other types of errors
  print("Something else went wrong")

# You can use the else keyword to define a block of
# code to be executed if no errors were raised:

try:
  print("Hello")
except:
  print("Something went wrong")
else: #if no errors occured, this will run.
    # The else block ONLY runs if the except did not run
  print("Nothing went wrong")
# it will run both the try and the else

# The finally block always runs regardless of everything else
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#The program can continue, without leaving the file object open

# Filter

# Map

# Lambda

# List Comprehension

# Dictionary Comprehension



#other:

'''
formated printing
print ('%.2f' %avg) this will print 2 decimal point float

'''
command = command.split() # to split a string into a list.
# split automatically uses whitespace but you can define anything you want

#you can construct a tuple by giving it an iterable list
#for example: mytuple = tuple(list)
#hash(mytuple) returns the hash of the tuple

#hash:



#alligning text:
'string'.ljust(20,'-')
#this will print string with 13 dashes to the right

'HackerRank'.center(20,'-')
#this will center HackerRank in the middle of the ----

print 'HackerRank'.rjust(20,'-')
# this will adjust it to the right of the ---


string.isupper() # will return true if upper case
string.islower() # will return true if lower case
# both return false if number or symbol

#use .upper() and .lower() to change to upper and lower

'potato'.join(list) #will combine elements of the list into a string with
#potato in ebtween each item.

#formatted printing in python:
print('hello %s %s' %(a, b)) #the list of arguments is in brackets
# after teh string you need %() () is a tuple with values. % is modulo operator

'''
How would you approach this?

One solution is to convert the string to a list and then change the value.
Example

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

Another approach is to slice the string and join it back.
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra

to replace a character:
def mutate_string(string, position, character):
    return (string[:position] + character + string[position+1:])


def count_substring(string, sub_string):
    a = len(sub_string)
    b = len(string)
    timz = 0
    for i in range(b-a+1):
        if string[i:a+i] == sub_string:
            timz +=1
    return timz

    ## the function above returns the number of times substring
    is found in string

checking strings:
.isalnum() checks if string is alpha numerical
.isalpha() check if only alphabets
.isdigit() checks if only digits 0-9
.islower() and .isupper()

to iterate multiple items

for num, cheese, color in zip([1,2,3], ['manchego', 'stilton', 'brie'], 
                              ['red', 'blue', 'green']):
    print('{} {} {}'.format(num, color, cheese))
prints

1 red manchego
2 blue stilton
3 green brie

a = [1, 2, 3, 4, 5] 
  
# printing the list using * operator separated  
# by space  
print(*a) 
  
# printing the list using * and sep operator 
print("printing lists separated by commas") 
  
print(*a, sep = ", ")  
  
# print in new line 
print("printing lists in new line") 
  
print(*a, sep = "\n")

args1 = list(map(int, (input().split())))
# create a map of int from list of string and convert to list



Cartesian Product

# Enter your code here. Read input from STDIN. Print output to STDOUT
args1 = list(map(int, (input().split())))
args2 = []
for i in range(args1[0]):
    templist = (list(map(int, (input().split()))))
    templist.pop(0)
    args2.append(templist)

args1 = [3, 1000] # testing
args2 = [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]] #testing
max_mod = 0
num_lists = args1[0]
modu = args1[1]
myresult = 0
mylength = len(args2)
print(args1)
print(args2)
print(mylength)

tot_list = []
tmp_list = []

for i in range(mylength-1): #0,1,
    for x in args2[i]: # 5 4
        for j in args2[i+1]: # 7 8 9
            tmp = x*x + j*j
            tmp_list.append(tmp) # 1 2 3 4 5 6
    args2[i+1] = tmp_list
    tmp_list = []

print(args2)
        


    
   # (args2[i]*args2[i])
    #max(enumerate(sub[i] for sub in l), key=itemgetter(1))

    #print('')


for x in args2[0]: #x = 5
    for i in args2[1]:
        for j in args2[2]:
            myresult = ((x*x) + (i*i) + (j*j))%modu
            if myresult > max_mod:
                max_mod = myresult
print(max_mod)
'''

#Cartesian Product:

'''
Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(int,(input().split())))
b = list(map(int,(input().split())))
c = list(product(a,b))
for i in range(len(c)):
    print(c[i], end =" ")

import itertools
a = [1,2,3,4,5]
b = [6,7,8,9,10]

c = []
c.append(a)
c.append(b)

d = list(itertools.product(a,b))
for i,x in enumerate(d):
    d[i] = d[i][0] + d[i][1]

print(d)

def secondmaxnum():
    n = int(input())
    arr = map(int, input().split())
    mylist = list(arr)
    maxi =  (max(mylist))
    maxii = -100

    for i in range(n):
        if mylist[i] < maxi and mylist[i] > maxii:
            maxii = mylist[i]
    print (maxii)


def namesofsecondlowestgrades():
    list1 = []
    minii_name = []
    minii = 100
    list2 = []

    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        list1.append([score,name])
    mingrade = (min(list1))[0]


    for i in range(n):
        if list1[i][0] > mingrade and list1[i][0] <= minii:
            minii = list1[i][0]
    
    for i in range(n):
        if list1[i][0] == minii:
            list2.append(list1[i][1])
    list2.sort()
    for i in range(len(list2)):
        print(list2[i])


def getaveragegrade():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    gradez = (student_marks[query_name])
    avg = round((sum(gradez)/3),2)
    print ('%.2f' %avg)
	
def checkstatusofletters:
    s = input()
    s_Length = len(s)
    bond = [False,False,False,False,False]
    for i in s:
        if i.isalnum() or bond[0]:
            bond[0] = True
        if i.isalpha() or bond[1]:
            bond[1] = True
        if i.isdigit() or bond[2]:
            bond[2] = True
        if i.islower() or bond[3]:
            bond[3] = True
        if i.isupper() or bond[4]:
            bond[4] = True
    print(*bond, sep = "\n")

Matrix in numpy

from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)
[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '11' '20' '22' '21']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']]

print(m[4][3]) (row then column)

linked lists:

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

Hash table in python is just a dictionary

BST:
The left sub-tree of a node has a key
less than or equal to its parent node's key.
The right sub-tree of a node has a key greater
than to its parent node's key.



'''





# how to create linkedlists in python

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

'''
textwrap.wrap() 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill() 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
'''

def print_formatted(number):
    # your code goes here
    spacepad = len((bin(n))[2:])
    for i in range(1,n+1,1):
        myarr = []
        myarr.extend([str(i).rjust(spacepad),
                    str((oct(i))[2:]).rjust(spacepad),
                    str((hex(i))[2:]).upper().rjust(spacepad),
                    str((bin(i))[2:]).rjust(spacepad)]
                    )

        print(*myarr)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
	
#To read 2 lines and print an output you can do this:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        ar = list(map(int, input().rstrip().split()))

        result = sockMerchant(n, ar)

        fptr.write(str(result) + '\n')

        fptr.close()



  
