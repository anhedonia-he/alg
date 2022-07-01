# @algorithm @lc id=1915 lang=python3 
# @title check-if-one-string-swap-can-make-strings-equal


from re import S

from numpy import sort
from en.Python3.mod.preImport import *
# @test("bank","kanb")=true
# @test("attack","defend")=false
# @test("kelb","kelb")=true
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        i = 0
        count = 0
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            return False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2:
                    return False
        return True if count == 2 else False