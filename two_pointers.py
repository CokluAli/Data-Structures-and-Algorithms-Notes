#  What is the Two-Pointer Pattern?

# Use two indices that move through the array from different directions.

# Most common setup:
# 	•	one pointer at the start
# 	•	one pointer at the end


left = 0
right = len(arr) - 1

while left < right:
    # do something with arr[left] and arr[right]
    left += 1
    right -= 1

arr = [1, 2, 3, 4]

# After function:
[4, 3, 2, 1]





arr = [1, 2, 3, 4]

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        #   1           4            4           1 
        left += 1
        right -= 1
        # += 1 moves a pointer forward, -= 1 moves a pointer backward.

        # If a function modifies a list in place, it usually does not return the list.





#-----------------#-----------------#-----------------#-----------------#-----------------#-------------------




#                                                  PALINDROME



# A palindrome reads the same forward and backward.

# Example:
# 	•	"racecar"


# What are we comparing?

# For a string:
s = "level"

# We want to compare:
# 	•	first char ↔ last char
# 	•	second char ↔ second last char
# 	•	and so on

# Same two-pointer idea, but instead of swapping:
# we compare


def is_palindrome(s):           
    left = 0
    right = len(s) - 1

    while left < right:        
        if s[left] != s[right]:
            return False
    
    left += 1
    right -= 1

    return True





# Given a sorted array, check if there are two numbers whose sum equals a target.

arr = [1, 2, 3, 4, 6]
target = 6

# Output:
True   # because 2 + 4 = 6



def two_sum_sorted(arr, target):
    left = 0 
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return True
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return False




#-----------------#-----------------#-----------------#-----------------#-----------------#-------------------




#                                                  SLIDING WINDOW


# Instead of:
# 	•	rechecking elements again and again

# We:
# 	•	keep a window of elements
# 	•	expand it
# 	•	shrink it
# 	•	update an answer as we go



# [ 2 | 3 | 1 ]  5  4
#   ↑         ↑
#  start     end


# Example:

arr = [2, 1, 5, 1, 3, 2]
k = 3

# Subarrays of size 3:
# 	•	[2, 1, 5] → sum = 8
# 	•	[1, 5, 1] → sum = 7
# 	•	[5, 1, 3] → sum = 9  correct
# 	•	[1, 3, 2] → sum = 6

# Output: 9


# When sliding the window by one step:
# 	•	subtract the element at the start of the previous window
# 	•	add the element at the end of the new window

# This is what makes the algorithm O(n) instead of O(n × k).




def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)


# When sliding the window,
# arr[i] enters and arr[i - k] leaves.
