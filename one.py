# Question 1 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.
#     def hello_name(user_name):

def hello_name(user_name):
    print(f'Hello_{user_name}!')

hello_name(user_name='Jay')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#   def first_odds():

def first_odds():
    for odds in range(1, 100, 2):
        print(odds)
        
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
#   def max_num_in_list(a_list):

def max_num_in_list(a_list):
    max_number = a_list[0]
    for number in a_list:
        if number > max_number:
            max_number = number

    return max_number

a_list = [13, 7, 1, 5, 9, 22, 15]
result = max_num_in_list(a_list)
print('The max number in a_list is:', result)


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
#       def is_leap_year(a_year):

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
    
year = 2020
result = is_leap_year(year)
print(f'Is {year} a leap year? {result}')


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
#    def is_consecutive(a_list):

def is_consecutive(a_list):
    if len(a_list) <= 1:
        return True
    
    sorted_list = sorted(a_list)
    for c in range(len(sorted_list) - 1):
        if sorted_list[c] + 1 != sorted_list[c + 1]:
            return False
    return True

a_list = [2, 4, 7, 8, 9, 10]
result = is_consecutive(a_list)
print('Is a_list consecutive?', result)

