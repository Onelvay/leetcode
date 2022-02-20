class Solution:
    def reverse(self, x: int) -> int:
        b=-2147483648
        if(x>0):
            x=int(str(x)[::-1])
        else:
            x=x*(-1)
            x=int(str(x)[::-1]) *(-1)
        if  b<x<(b)*(-1):
            return x
        else: 
            return 0
