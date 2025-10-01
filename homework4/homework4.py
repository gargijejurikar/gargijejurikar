# 3.1: List Operations
favorite_foods = ["mangos", "strawberries", "lychees", "watermelon", "cantaloupe"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("blackberries")
favorite_foods.insert(0, "apple")
favorite_foods.remove("lychees") 

# I got an error here:
# Traceback (most recent call last):
#   File "c:\Users\jejur\python_decal_fa25\gargijejurikar\homework4\homework4.py", line 7, in <module>
#     favorite_foods.remove(2)
#     ~~~~~~~~~~~~~~~~~~~~~^^^
# ValueError: list.remove(x): x not in list
# because i used the index instead of the value. fixed it by changing to favorite_foods.remove("lychees")

print(len(favorite_foods))
for item in favorite_foods:
    print(item.upper())
new_list = favorite_foods[0::5]
print(new_list)

def is_a_potato(list): # ran in git bash!
    potato = "potato"
    if potato in list:
        return "A potato!"
    else:
        return "No potato!"
    
print(is_a_potato(favorite_foods))

# 3.2: Slicing and Striding
numbers = list(range(0,21))
print(numbers)
def get_first_15(num): 
    return(num[0:15:])
def get_every_5th(lst):
    return(lst[0::5])
def reverse_and_stride(lst):
    backwards = lst[::-1]
    return(backwards[::3])
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step3) # ran in git bash as compiled function

# 3.3: Nested Lists
numbers_nested = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(numbers_nested[2])
# I got this error when I tried to call my nested list:
# Traceback (most recent call last):
#   File "c:\Users\jejur\python_decal_fa25\gargijejurikar\homework4\homework4.py", line 48, in <module>
#     numbers = [[1, 2, 3]
#                ~~~~~~~~~
#                [4, 5, 6]
#                ^^^^^^^^^
# TypeError: list indices must be integers or slices, not tuple
# resolved the error, I forgot commas between nested lists
print(numbers_nested[1][1])
numbers_nested.append([10,11,12])
print(numbers_nested)
def sum_nested(nestedlist):
    return(sum(sum(sublist) for sublist in nestedlist))
print(sum_nested(numbers_nested))
# I got this error here:
# Traceback (most recent call last):
#   File "c:\Users\jejur\python_decal_fa25\gargijejurikar\homework4\homework4.py", line 69, in <module>
#     print(sum_nested(numbers))
#           ~~~~~~~~~~^^^^^^^^^
#   File "c:\Users\jejur\python_decal_fa25\gargijejurikar\homework4\homework4.py", line 67, in sum_nested
#     sum += item
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'
# this is because it was adding sublists to an integer (i think?). I fixed this by summing the sublists first.

# 3.4: Create a 5x5 List
def five_by_five():
    numbers = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        numbers.append(row)
    return numbers
matrix = five_by_five()

def multiples_of_3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
            j += 1
        i += 1
    return matrix
new_matrix = multiples_of_3(five_by_five())
print(new_matrix)

def add_elements(matrix_no_3):
    result = 0
    for i in range(len(matrix_no_3)):
        for j in range(len(matrix_no_3)):
            if matrix_no_3 [i][j] != "?":
                result += matrix_no_3[i][j]
            j += 1
        i += 1
    return result
sums_no_threes = add_elements(new_matrix)
print(sums_no_threes)

# 4 Dictionaries
# 4.1 Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100 # changing Mira's age to 100
ages["Milana"] = 52 # adding Milana with age 52
for key, value in ages.items():
    print(f"{key},{value}")

# 5.1 VS Code
#   problems completed!!

# 5.2 In Your VS Code Terminal:
sum_total = add_elements(new_matrix) # this is my favorite function because I figured it out without outside help and I initially thought it was too hard for me to do :)
print(sum_total)