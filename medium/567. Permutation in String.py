class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        a=''.join(sorted(s1))
        print(a)
        for i in range(len(s2)-len(s1)+1):
            if a==''.join(sorted(s2[i:i+len(s1)])):
                 return True
        return False


