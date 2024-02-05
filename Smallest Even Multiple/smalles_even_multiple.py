class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        lcm =0
        if n%2==0:
           lcm=n;
        elif n%2!=0:
             lcm=2*n
        return lcm
