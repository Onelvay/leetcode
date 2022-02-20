class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        nums=list(itertools.permutations(nums))
        return nums
