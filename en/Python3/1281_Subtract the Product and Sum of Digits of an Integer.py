# @algorithm @lc id=1406 lang=python3 
# @title subtract-the-product-and-sum-of-digits-of-an-integer


from en.Python3.mod.preImport import *
# @test(234)=15
# @test(4421)=21
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        product, sum = 1, 0
        for i in range(len(n_str)):
            product = product * int(n_str[i])
            sum = sum + int(n_str[i])
        
        return product - sum