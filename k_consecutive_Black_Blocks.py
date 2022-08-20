'''
Minimum Recolors to Get K Consecutive Black Blocks

'''
import time
def minimumRecolors(blocks, k):
    best =  10 **20
    '''
    WBBWWWBWBBW
    <->
     <-> sliding window concept
   '''
    current = 0
    N = len(blocks)
    for i in range(N):
        if blocks[i] == "W":
            current += 1
        if i-k >=0 and blocks[i-k] == "W":
            current -=1       
        if i-k+1 >=0:
            best = min (best,current)    
    return best
start = time.time()
K = int(input())
block = input().upper()
result = minimumRecolors(blocks = block, k = K)
print(result)
end = time.time()
print(end-start)

