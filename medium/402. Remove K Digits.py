class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans=[]
        for i in num:
            while k>0 and ans and ans[-1]>i:
                k-=1
                ans.pop()
            ans.append(i)
            
        ans=ans[:len(ans)-k]
        ans=''.join(ans)
        return str(int(ans)) if ans else '0'
        
