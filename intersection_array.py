
def intersect(nums1, nums2):

    save = []
        
    for i in nums1:
            
        if i in nums2:
                
            save.append(i)
                
            nums2.remove(i)
        
    return save

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

result_list = intersect(nums1, nums2)

print(result_list)
