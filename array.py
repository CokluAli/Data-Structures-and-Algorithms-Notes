
#  Static Array vs Dynamic Array 

#  Static Array
# 	•	Size is fixed
# 	•	Cannot grow or shrink
# 	•	Must decide size in advance

# Example (C / Java style):

# array of size 5 → always size 5

# If it’s full:
# 	•  You can’t add more elements





# Dynamic Array
# 	•	Size can grow and shrink
# 	•	Internally resizes itself
# 	•	Easier to use

# This is what Python lists are.



# A Python list is a dynamic array.
# Example:
# arr = [1, 2, 3]
# arr.append(4)

# Behind the scenes:
# 	•	Python creates a bigger array
# 	•	Copies elements
# 	•	Adds the new value

# You don’t see this — Python handles it.



#  Why resizing matters (intuition only)

# When you do: arr.append(x)

# Most of the time:
# 	•	⏱ O(1)

# But sometimes:
# 	•	Python must resize
# 	•	Copy all elements
# 	•	⏱ O(n)

# Because this doesn’t happen often, we say:

# Amortized O(1)


def get_last_element(arr):
    return arr[-1]

def get_middle_element(arr):
    return arr[len(arr) // 2]

def sum_first_and_last(arr):
    return arr[0] + arr[-1]




def count_greater_than_5(arr):
    counter = 0
    for x in arr:
        if x > 5:
            count =+1
    return counter



arr = [1, 3, 5, 7]
target = 5

def if_exists(arr, target):
    for x in arr:
        if x == target:
            return True
    return False



def get_even_numbers(arr):
    evens = []
    for x in arr:
        if x % 2 == 0:
            evens.append(x)
    return evens

# Time Complexity: O(n)




#-------------------------------------------------



def count_char(s, target):
    count = 0
    for ch in s:
        if ch == target:
            count += 1
    return count



def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result

# Time Complexity: O(n)



def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

# Time Complexity: O(n)




#-------------------------------------------------


def add_to_end(arr, x):
    arr.append(x)
    return arr



def remove_last(arr):
    arr.pop()
    return arr 
# time complexity o(1)

def remove_last(arr):
    return arr.pop()

# Time Complexity: O(1)


#-------------------------------------------------


def remove_at_index(arr, i):
    return arr.pop(i)

# Time Complexity: O(n)


# pop(i) does two things:
# 	1.	Removes the element at index i
# 	2.	Returns that removed element





#  .insert(index, value)
    # 	•	Inserts a value at a specific index
    # 	•	Shifts everything to the right


arr = [1, 2, 3]
arr.insert(1, 99)
# arr → [1, 99, 2, 3]



def insert_at_index(arr, i , x):
    arr.insert(i, x)

# time complexity = o(n)


arr = [10, 20, 30]
insert_at_index(arr, 1, 99)

# arr → [10, 99, 20, 30]


#-------------------------------------------------

# arr = [1, 2, 3, 2]
# arr.remove(2)
# # arr → [1, 3, 2]


def remove_value(arr, x):
    arr.remove(x)





def count_even_numbers(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count +=1
    return count
# time complexity o(n)




def greater_than_3(arr):
    result = []
    for x in arr:
        if x > 3:
            result.append(x)
    return result


# time complexity o(n)



def sum_greater_than_5(arr):
    sum = 0
    for x in arr:
        if x > 5:
            sum += x
    return sum

# time complexity o(n)





#-------------------------------------------------





def count_long_strings(arr):
    count = 0
    for x in arr:
        if len(x) > 3:
            count += 1
    return count

# time complexity o(n)


def has_negative(arr):
    for x in arr:
        if x < 0:
            return True
    return False
# time complexity o(n)



#-------------------------------------------------#-------------------------------------------------



#  What is a list comprehension?

#        A list comprehension is a compact way to build a new list from an existing one.




# The general structure 

# [ expression for item in iterable if condition ]

# Breakdown:
# 	•	expression → what you add to the new list
# 	•	item → each element
# 	•	iterable → the list you loop over
# 	•	condition → optional filter


# The basic syntax for a list comprehension is enclosed in square brackets [] and includes an expression followed by a for clause. 




def get_even_numbers(arr):
    result = []
    for x in arr:
        if x % 2 == 0:
            result.append(x)
    return result


even_numbers = [x for x in arr if x % 2 == 0]
# this will be -> -> 

def get_even_numbers(arr):
    return [x for x in arr if x % 2 == 0]

# Is conceptually equivalent to:

# _temp = []
# for x in arr:
#     if x % 2 == 0:
#         _temp.append(x)



#         A list compes .append() under the hoorehension still usd.



# The first x means:

# “What do I add to the new list?”

# So:
# 	•	every time the condition is true
# 	•	that first x is appended to the result list




def get_lengths(arr):
    result = []
    for x in arr:
        result.append(len(x))
    return result


def get_lengths(arr):
        return [len(x) for x in arr]






# result = []

# for x in arr:
#     if x % 2 == 1:      # odd number
#         result.append(x * x)
# return result



def square_odds(arr):
    return [x*x for x in arr if x % 2 == 1]




# [EXPRESSION for x in iterable if CONDITION]


# 	•	CONDITION decides whether to keep x
# 	•	EXPRESSION decides what value gets added





def double_gt_4(arr):
    return [x * 2 for x in arr if x > 4]





def first_chars(arr):
    return [x[0] for x in arr]



def long_upper(arr):
    return [x.upper() for x in arr if len(arr) > 3]



def last_chars(arr):
    return [x[-1] for x in arr if len(arr) >= 2]