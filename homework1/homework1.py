# File: homework1. py

# ---Variables and Data Types---
a=10
print(a)
print(type(a))
# a is an integer - a whole number without a decimal

b=1.5
print(b)
print(type(b))
# b is a float - a real number with a decimal

c=3j
print(c)
print(type(c))
# c is a complex number - j is the square root of -1

d="hello"
print(d)
print(type(d))
# d is a string - a combination of letters

e=[1,2,3]
print(e)
print(type(e))
# e is a list - a set of numbers separated by commas

f={"name": "Ellen","favorite fruit":"strawberry"}
print(f)
print(type(f))
# f is a dictionary - storage of key-value pairs

g=(1,2)
print(g)
print(type(g))
# g is a tuple - unchangeable parameters once created

h=["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list - ordered strings separated by commas

i=True
print(i)
print(type(i))
# i is a boolean value - must be either true or false

j=None
print(j)
print(type(j))
# j is a nonetype - indicates no value

k=[True, "blue", 12]
print(k)
print(type(k))
# k is list - separated by commas, collection of different types of values

l=str(14)
print(l)
print(type(l))
# l is a string - the str converts the integer 4 into a string

m=1e4
print(m)
print(type(m))
# m is a float - number with a decimal

"""
 1. 9 different types of data types
 2. integer, float, string, list, dictionary, boolean, nonetype, tuple, complex number
 3. b and m are both floats, d and l are both strings, e and h are both lists
 4. l was a string. It was not an integer because using the str() function converted it from an integer to essentially text.
 5. set, used below with var n
"""

n={"red", "yellow","blue"}
print(n)
print(type(n))
# n is a set  - multiple variables are not given a specific order

# ---Booleans---
print(10>9) # TRUE
print(10==9) # FALSE
print(10<=9) # FALSE
print(bool("abc")) # TRUE
print(bool(123)) # TRUE
print(bool(["apple","cherry","banana"])) # TRUE
print(bool(True)) # TRUE
print(bool(False)) # FALSE
print(bool(0)) # FALSE
print(bool("")) # FALSE
print(bool(" ")) # TRUE
print(bool(())) # FALSE
print(bool([])) # FALSE
print(bool({})) # FALSE
print(bool(True and False)) # FALSE
print(bool(True and True)) # TRUE
print(bool(True or False)) # TRUE
print(bool(True or True)) # TRUE
print(bool(False or False)) # FALSE
print(bool(not(False))) # TRUE
print(bool(not(True))) # TRUE

"""
1. All terms must be TRUE, or else the result is FALSE.
2. I was surprised with the parentheses, because I have no idea what they mean.
3. bool(10+10=20) it is true because both sides of the equal sign are equal.
4. bool(True = False) because true and false are not the same.
"""

# ---Operators---
print(10+5) #15, performs addition
print(10-5) #5, performs subtraction
print(2*4) #8, performs multiplication
print(6/3) #2, performs division
print(5%2) #1, returns remainder of division
print(3**2) #9, squares
print(15//2) #7, divides numbers and rounds down
print(5==2) #FALSE, this inequality is incorrect (5!=2)
print(10!=10) #FALSE, this inequality is incorrect (10==10)
print(2<5) #TRUE, this inequality is correct
print(12>5) #TRUE, this inequality is correct
print(5<=6) #TRUE, this inequality is correct
print(1>=10) #FALSE, this inequality is incorrect.

x = 5
print(x)
x += 5
print(x)
x -= 4
print(x)
x *= 3
print(x)

"""
1. the operator "and" requires both conditions to be satisfied. 4<5 and 5<6; 4<5 and 5>6
2. the operator "or" requires one condition to be satisfied. 4<5 or 5>6; 5>6 or 6>7
3. the operator "not" inverts true and false values. not 4>5; not 4<5

1. / returns the result of division, while // returns the result of division rounded down to the closest integer.
2. % returns the remainder of division, while // is the quotient rounded down to the clostest integer.
3. I would use %; for example, print(7%3) would return 1.
4. assignment operators assign values to variables. for example, += adds a value to the previous value of the variable, and from then on the variable is the new one.
"""

# ---Strings---
my_string ="hello"
print(my_string) #prints hello
print(my_string[0]) #prints h
print(my_string[1]) #prints e
print(my_string[2]) #prints l
print(my_string[3]) #prints l
print(my_string[4]) #prints o
print(my_string[-1]) #prints o
print(my_string[1:3]) #prints el
print(my_string[0:5:2]) #prints hlo
print(len(my_string)) #prints 5
print(my_string+"goodbye") #prints hellowgoodbye
print(my_string*7) #prints hellohellohellohellohellohellohello

"""
1. string slicing is printing parts of a string by specifyign where to start and end. used this for  #2-9
2. see below
3. see below
4. f-strings are ways to embed expressions inside strings (put a variable inside a string)
"""
name = "Oski"
print("hello, my name is" + name) #prints string plus Oski

name = "Oski"
print(f"Hello, my name is {name}") #this one incoroporates the variable name into the string instead of adding it separately

# ---Terminal Commands---
"""
1. cd - changes directories, move from one folder to another - cd gargijejurikar
2. ls - lists the files or directories in current directories - ls python_decal_fa25
3. ls -a - lists all files/directories including hidden ones - ls -a desktop
4. mkdir - creates directory - mkdir homework_folder
5. cat - opens text file - cat test.py
6. pwd - prints current working directory - pwd
7. cd .. - navigates up one directory level - cd ..
8. cd . - changes to current directory (does nothing)
9. cd ~ - changes to root directory
10. cp - copies files and directories
11. mv - moves files or directories
12. rm - deletes (removes) files or directories
13. clear - clears terminal screen (not any data)
14. grep - basically ctrl + f for code
"""

"""
1. touch: creates file; man: prints manual/get help; rmdir: remove empty directories
2. ls lists files and directories within the current working directory, ls -a also lists "hidden" files and directories.
3. they usually begin with a . and are not restricted, just hidden from view.
4.  ls -l prints contents of current directory in long form (shows more details); touch -d allows you to set a timestamp for the file; mkdir -p creates parent directories
"""