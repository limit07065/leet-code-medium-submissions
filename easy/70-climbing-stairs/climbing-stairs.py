class Solution:
    def climbStairs(self, n: int) -> int:
        if n is 1:
            return 1
        elif n is 2:
            return 2
        else:
            totalb2 = 1
            totalb1 = 2
            total = 3
            for i in range(2,n):
                total = totalb2 + totalb1
                totalb2 = totalb1
                totalb1 = total
            return total
        
        