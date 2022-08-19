
def twoSum( nums, target):
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:
        
                    return [i,j]
        
nums = list(map(int, input().split()))

target = int(input())

result = twoSum(nums, target)

print(result)
        
        # visited={}
        
        # for i in range(len(nums)):
            
        #     sec_num=target-nums[i]
            
        #     if sec_num in visited:
                
        #         return[i,visited[sec_num]]
            
        #     else:
                
        #         visited[nums[i]]=i
