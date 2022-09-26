class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key=strs[0]
        res=""
        for i in strs:
            if(len(i)<len(key)):
                key=i
        for i in range(0,len(key)):
            b=False
            for j in strs:
                if(key[:i+1]!=j[:i+1]):
                    b=True
            if(b==False):
                res=key[:i+1]
        return(res)