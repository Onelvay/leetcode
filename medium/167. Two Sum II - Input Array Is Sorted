class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k=len(numbers)-1
        l=0
        while(l<k):
            sum=numbers[l]+numbers[k]
            if(sum<target):
                l+=1
            elif sum>target:
                k-=1
            else:
                return ([l+1,k+1])
        return []
        
        
