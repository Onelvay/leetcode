class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        ans=0
        sums={0:1}

        for i in nums:
            sum+=i
            if sum-k in sums:
                ans+=sums[sum-k]
            if sum in sums:
                sums[sum]+=1
            else:
                sums[sum]=1
        return ans
