class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=0
        count=[]
        if(k==0):
            for i in range(len(nums)-1):
                for j in range(i+1,len(nums)):
                    if abs(nums[j]-nums[i])==k and nums[i] not in count:
                        count.append(nums[i])
                        ans+=1
        else:
            diff=list(set(nums))
            for i in range(len(diff)):
                if diff[i]+k in diff:
                    ans+=1
        return ans

        
