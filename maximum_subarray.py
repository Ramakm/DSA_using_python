# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


        
"""
        Time complexity: O(N)
        Space complexity: O(1)
      
        Steps:
        1. Initialize "sum_counter" to be first element of list
        2. Let current largest sum also be equal to the first element of list
        3. Iterate over the entire list starting from index 1 (since sum of index 0 element is already added to sum_counter)
        
            a. Set "sum_counter" to the maximum between the:
                "i-th list element" or "sum of the i-th list element and previous value of sum_counter" 
                (Idea here: If nums[i] increases sum_counter, keep the cumulative sum value going
                            Else, set the sum_counter to nums[i])
            
            b. if current sum_counter is greater than largest_sum value:
                set largest_sum to sum_counter
"""
def maxSubArray(nums):
    sum_counter = nums[0]
    largest_sum = sum_counter

    for i in range(1, len(nums)):
        sum_counter = max(sum_counter + nums[i], nums[i])
        if sum_counter > largest_sum:
            largest_sum = sum_counter
    return largest_sum


list = input().split()


result = maxSubArray(nums = list)
print(result)