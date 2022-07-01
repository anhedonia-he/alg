# @algorithm @lc id=202 lang=python3 
# @title happy-number


from en.Python3.mod.preImport import *
# @test(19)=true
# @test(2)=false
class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        seen = set()

        def get_next(n):
            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

