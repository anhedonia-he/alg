# @algorithm @lc id=1894 lang=python3 
# @title merge-strings-alternately


from en.Python3.mod.preImport import *
# @test("abc","pqr")="apbqcr"
# @test("ab","pqrs")="apbqrs"
# @test("abcd","pq")="apbqcd"
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        for i in range(len(word1)):
            output.append(word1[i])
