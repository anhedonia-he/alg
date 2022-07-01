# @algorithm @lc id=1797 lang=python3 
# @title goal-parser-interpretation


from en.Python3.mod.preImport import *
# @test("G()(al)")="Goal"
# @test("G()()()()(al)")="Gooooal"
# @test("(al)G(al)()()G")="alGalooG"
class Solution:
    def interpret(self, command: str) -> str:
        result = []
        index_of_left = 0
        for i in range(len(command)):
            result.append(command[i])
            if command[i] == "(":
                index_of_left = i
            if command[i] == ")" and command(i-1) == "(" :
                result.pop()
                result.pop()
                result.append("o")
            else:
                result.pop()
                result.remove(command[index_of_left])

        return str(result)