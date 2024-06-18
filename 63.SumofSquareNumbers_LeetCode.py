import random

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
       # optimized solution
        # a and b must be greater than c, a and b could be 0
        # a^2 = c, a = square root of c
        # create two points to check numbers in array [0,sqrt(c)]
       
       left, right = 0, int(sqrt(c))
       while left <= right:
            total = left * left + right * right
            if total > c: # shrink range
                right -= 1
            elif total < c:
                left += 1
            else:
                return True
       return False
       
       """ # randomly get numbers up to c
        # put pair in set if not seen
        # check if a^2 + b^2 = c
    
        seen = {}
        flag = False

        if c == (1,2,3,4):
            return False

        while flag is False:
            a = randrange(1,c)
            b = randrange(1,c)
            if ((a,b) not in seen):
                seen.update(a,b)
                if ( (a^2) + (b^2) ) == c:
                    flag = True

        return True"""
