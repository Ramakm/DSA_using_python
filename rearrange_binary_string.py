'''
# Time Needed to Rearrange a Binary String

'''
import time
def secondstoremoveoccurances(s):
    N = len(s)
    if "0" not in s:
        return 0 
    count =0
    while "01" in s:
        s = s.replace("01", "10")
        count += 1
    return count

start = time.time()
string1 = input()
result = secondstoremoveoccurances(s = string1)
print(result)
end = time.time()

print(end-start)
