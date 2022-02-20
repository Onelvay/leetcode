class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        itog=[]
        def result(i=0):
            if i==len(nums):
                itog.append(ans.copy())
                return 
            ans.append(nums[i])
            result(i+1)
            ans.pop()
            result(i+1)
        result()
        return (itog)
        
