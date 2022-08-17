def firstUniqChar(s):
             
        
    new_set = {}
   
        
    for c in s:
            
        if c not in new_set:
            new_set[c] = 1
        else:
            new_set[c] += 1
                
    for i in range(len(s)):
        if new_set[s[i]] == 1:
            return i
            
    return -1

string = input()

result = firstUniqChar(s = string)
print(result)