# 3.1: Vocab Review
# 1. git is the command line that runs locally, github is a web-based place to store repositories
# 2. terminal is where your code runs, command line is where you execute it
# 3. local repository is stored on your device, while remote is stored elsewhere like the web
# 4. version control is keeping track of the updates made to your code/files
# 5. staging area is where your changes go before being saved/committed
# 6. git add tracks new changes/sends to staging area
# 7. git commit commits new changes made "saves" them
# 8. git push pushes these changes to a remote repository
# 9. git status tells you about your working directory and staging area
# 10. git pull downloads content from a remote repository
# 11. pwd "print working directory" file path to where you are
# 12. ls "list" what's in hte folder you're working in
# 13. cd "call directory" move into different directory/folder
# 14. nano opens python editor in command line
# 15. creates a new file 
# 16. mv "move" file to a new location
# 17. rm "remove" delete a file
# 18. cat displays file content

# 3.2: A Directory Tree
"""
1. pwd
2. ls
3. cd ../brianna_repo
    git pull 
4.  mv homework.py ../judy_decal/
5. cd ../judy_decal/
6. nano homework.py
7. judy pushed before pulling so local repository was out of sync with remote one
8. ~/Recent/
"""

# 4.1: Data Types
def check_data_type(value):
    return type(value).__name__ 
print(check_data_type(3.14))
print(check_data_type(True))

# 4.2: Conditionals
def even_or_odd(num):
    if num%2 ==0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(7))
print(even_or_odd(10))

# 5. Loops
def sum_of_numbers(numlist):
    total = 0
    for num in numlist:
        total += num
    return total
numbers = [1,2,3,4,5]
print(sum_of_numbers(numbers))

# 6.1 Lists
def duplicate_list(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list
print(duplicate_list(["a","b","c"]))

# 6.2 Debugging
def square(num):
    return num*num
print(square(3)) # missing : after defining function

list1 = [3,2,4,7,5,3,6,8,3,5]
print(sum_of_numbers(list1))