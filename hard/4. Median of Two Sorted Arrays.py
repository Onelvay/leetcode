class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=sorted(nums1+nums2)
        k="{:."+str(5)+"f}"
        if(len(nums3)%2==1):
            c=float(k.format(nums3[len(nums3)//2]))
            return(c)
        else:
            a=nums3[(len(nums3)//2)-1]
            b=nums3[(len(nums3)//2)]
            c=float(k.format((a+b)/2))
            return(c)
        
