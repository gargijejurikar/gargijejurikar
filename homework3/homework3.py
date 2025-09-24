# 3.1: Say Goodbye
def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("gargi") # prints "Goodbye, gargi"

# 3.2: Area of a Circle
def area_of_circle(radius):
    print(3.14*radius**2)
area_of_circle(2)

# 4.1: Subtract, Multiply, and Divide
def subtract(num1, num2):
    return(num1-num2)
print(subtract(4,3))

def multiply(factor1, factor2):
    return(factor1*factor2)
print(multiply(4,3))

def divide(dividend,divisor):
    return(dividend/divisor)
print(divide(12,4))

# 5.1: What Should I Wear?
temperatures = [68, 65, 64, 62, 70, 86, 92, 86]
def temp_min_and_max(result):
    return(min(temperatures), max(temperatures))
print(temp_min_and_max(temperatures))

# 5.2: Check if it's the Weekend
def is_weekend(day_number):
    if day_number>=6: # where monday = 1, sunday = 7 and everything in between
        return("True")
    else:
        return("False")
print(is_weekend(4))

# 5.3: Fuel Efficiency Calculator
def determine_fuel_efficiency(distance,fuel):
    return(distance/fuel)
print(determine_fuel_efficiency(400,40)) # returns miles per gallon as an integer

# 5.4: Secret Code
def secret_code_maker(num):
    last_digit = num%10
    rest_of_digits = num//10
    digits = len(str(rest_of_digits))
    return(last_digit*(10**digits)+rest_of_digits)
print(secret_code_maker(12345))

# 6.1: Oski Stole Your Power
def power(x,y):
    result = 1 # defines a result we can multiply x times
    for _ in range(y): # arbitrary variable defined by y
        result*=x # multiplies it by x, y times
    return result
print(power(4,3))

# 6.2: Min and Max with Loops
# 6.2.1: For Loops
numbers_list_for = [3, 5, 1, 7, 28, 3, 9]

def minimum_value_for(data_min_for):
    minimum_value = data_min_for[0] #starts off with first value
    for num in data_min_for: # takes values in data list
        if num < minimum_value: # compares each number to previously determined minimum value
            minimum_value = num # num becomes new smallest value if smaller number is found
    return(minimum_value)
print(minimum_value_for(numbers_list_for))

def maximum_value_for(data_max_for):
    maximum_value = data_max_for[0]
    for num in data_max_for:
        if num > maximum_value:
            maximum_value = num
    return(maximum_value)
print(maximum_value_for(numbers_list_for)) # YIPPEE IT FINALLY WORKS IM SO COOL AND SMART

# 6.2.2: While Loops
# we need to compare each number to our initial number and see if it's larger/smaller
# if true then we reassign the new number to be the smallest
# we'll move through the list using an index
numbers_list_while = [3, 4, 2, 9, 12, 9, 10]
def minimum_value_while(data_min_while):
    min_value = float('inf') # starts minimum value as positive infinity so first number will always be smaller
    index = 0 # keeps track of the position in the lsit
    while index < len(numbers_list_while): # keeps loop going until index is less than the length of the list
        current_num = numbers_list_while[index] # assigns current value to position in the data list
        if current_num < min_value: # compares current value to previously determined minimum value
            min_value = current_num # assigns current value as new minimum if true
        index += 1 # adds 1 to index to move through list
    return(min_value) #returns the determined minimum
print(minimum_value_while(numbers_list_while)) # returns 2 which is the correct answer  YAY

def maximum_value_while(data_min_while):
    max_value = float('-inf') # starts maximum value as -infinity so first number will always be larger
    index = 0
    while index < len(numbers_list_while):
        current_num = numbers_list_while[index]
        if current_num > max_value:
            max_value = current_num
        index += 1
    return(max_value)
# the rest of this function works the same as the previous function, just comparing to see if the number is larger rather than smaller
print(maximum_value_while(numbers_list_while))

# 6.3: Calculate the Sum
# we want this function to take an integer and return the sum of its digits
# to do this we need to take progressive remainders by dividing by factors of 10 to yield each digit individually
# we need to make a loop that goes through the integer doing this. probably a while loop using the len function
# the hard part of this is making it divide by 10 repetitively!
def sum_of_digits(num):
    digit_sum = 0 # starting off our result at 0 so we have something to add to
    while num > 0: # this ensures we go through our whole list until there are no more digits in our initial number
        digit = num % 10 # gives remainder which is the last digit
        digit_sum += digit # update our result with the digit we just separated
        num //= 10 # updates number by dividing by 10 and rounding down (gets rid of last digit)
    return(digit_sum)
print(sum_of_digits(2468)) # returns 20 YIPPEE

# 7.1 
long_integer = 7249723804
result = sum_of_digits(long_integer)
print(f"The result of Calculate the Sum (6.3) with long_integer = {long_integer} is {result}.")