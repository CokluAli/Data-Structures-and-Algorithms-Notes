# Big O (Time Complexity):
# Big O describes how the running time of a program grows
# when the input size (n) becomes larger.
# It does NOT measure exact speed, only growth.

# n:
# n usually means the number of items in the input
# (for example, the length of a list).
# n is the size of the input (for example, the number of items in a list).

# O(1) - Constant Time:
# The program always does the same amount of work,
# no matter how big the input is.
# Example: accessing an element by index in a list.

# O(n) - Linear Time:
# The program does more work as the input gets bigger.
# If the input size doubles, the work also doubles.
# Example: looping through a list once.

# O(n^2) - Quadratic Time:
# The program uses nested loops.
# For each element, it loops through the input again.
# This becomes slow for large inputs.
# Example: comparing every element with every other element.

# O(log n) - Logarithmic Time:
# The program reduces the problem size by half each step.
# The input gets smaller very quickly.
# Example: binary search on a sorted list.

# O(n log n) - Linearithmic Time:
# The program divides the problem into smaller parts
# and processes all elements at each level.
# Example: merge sort.

# Why Big O matters:
# It helps us compare algorithms and choose efficient ones,
# especially for large inputs.
# It helps us avoid slow solutions that do not scale well.




#  --------------O(1)--------------------------------------------
 

# O(1) - Constant Time:
# The function always does the same amount of work,
# no matter how big the input is.
# The number of operations does NOT change when the input grows.
# There are no loops or repeated steps.
# O(1) means the amount of work does not increase when input size increases
# The function must do the same amount of work even when the input gets bigger.


def middle_element(arr):
    return arr[len(arr) // 2]


def firt_and_last(arr):
    return arr[0] + arr[-1]


def example(arr):
    return arr[0]

# Time Complexity: O(1)
# Reason: The function accesses one element directly.
# It does not loop or repeat work when the list gets bigger.


def take_i(arr, i):
    return i
    


#------------------------------------------------------------------------------------------







# --------------O(n)--------------------------------------------




# O(n)
# O(n) - Linear Time:
# The function does more work as the input gets bigger.
# If the input size doubles, the work also doubles.
# The number of operations grows linearly with the input size.
# The function usually has a single loop that goes through all items once.

#If I touch every element once → O(n)


def count_greater_than_10(arr):
    count = 0
    for x in arr:
        if x > 0:
            count += 0
    return count
        


def find_largest_number(arr):
    number = 0
    for x in arr:
        if x > number:
            number = x
    return number
 
# > >

def find_largest_number(arr):
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
    return largest

# has a single loop that goes through each element - each element is compared once - more element -> more work



def is_exist(arr):
    for x in arr:
        if x == 5:
            return True
    return False
# every element is checked, time complexity. O(n)



def sum_of_numbers(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum



#  Loop with a fixed number (like 5, 10, 100) → O(1)
#  Loop that depends on input size (like for x in arr) → O(n)


#------------------------------------------------------------------------------------------
















# --------------O(n^2) Quadratic Time:--------------------------------------------


# O(n²) happens when for each element, you loop over the elements again.
#  	one loop inside another loop
#	work grows very fast


# Not every nested loop is O(n²).
# It’s O(n²) only when both loops depend on n.



arr = [1, 2, 3]

for x in arr:
    for y in arr:
        print(x, y)
    print()



arr = [1, 2, 1]

def count_equal_pairs(arr):
    equal_numbers = 0

    for x in arr:
        for y in arr:
            if x == y:
                equal_numbers += 1

    return equal_numbers




arr = [1, 2, 3]

def pair_different_numbers(arr):
    different_numbers = 0

    for x in arr:
        for y in arr:
            if x != y:
                print(x, y)
        print()






arr = [3, 7, 5, 5]

def sum_of_pairs_equal_to_10(arr):
    sum = 0

    for x in arr:
        for y in arr:
            if x + y == 10:
                sum += 1
    return sum


#------------------------------------------------------------------------------------------
















# --------------O(log N) Logarithmic Time:--------------------------------------------


#O(log n) means the problem size is cut in half each step.

# We are not checking everything.
# We are throwing half away again and again.


# Binary search works only on a sorted list.

# Example:
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7  


# Look at the middle → 7
# Is it the target? → YES
# Done.

# Only one check.



# Another example (target = 3)

#  Middle is 7
# 	•	3 is smaller → ignore the right half

#  New list: [1, 3, 5]
# 	•	Middle is 3 → found


# 	•	didn’t check every number
# 	•	threw away half each time



#        If each step cuts the input in half → O(log n)

# O(log n):
# The input size is cut in half at each step.




arr = [1, 3, 5, 7, 9]
target = 3


def find_target(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False






arr = [2, 4, 6, 8, 10, 12]
target = 10

def find_target(arr, target):
    left = 0 
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False


# Time Complexity: O(log n)
# Reason: The search space is cut in half each iteration.

# 	/ → normal division → gives a float
#  *  // → floor division → gives an integer

# That’s why binary search always uses //.




arr = [1, 4, 6, 9, 13, 18]
target = 6


def find_target(arr, target):
    left = 0
    right = len(arr) -1 

    while left <= right:
        mid = (right + left) // 2

        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            right = mid - 1 
        else:
            left = mid + 1

    return False
            



#------------------------------------------------------------------------------------------
















# --------------O(N log N) Linearithmic Time:--------------------------------------------





# O(n log n) = divide the problem (log n) + process everything (n)

# It’s basically:
# 	    break the problem into smaller pieces
# 		then do linear work to combine results



# The array we want to sort
arr = [4, 1, 3, 2, 8, 5]


def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Finds the middle of the array
    mid = len(arr) // 2

    # Splits the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sorts both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merges the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Runs merge sort
sorted_arr = merge_sort(arr)

# Prints result
print("Original array:", arr)
print("Sorted array:", sorted_arr)