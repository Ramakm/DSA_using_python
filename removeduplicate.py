#Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(nums):
        
    new_set = set() 
        
    for num in nums:
            
        if num in new_set:
            return True
            
        else:
                
            new_set.add(num)
                
            return False


list1 = input().split()

print(containsDuplicate(nums = list1))