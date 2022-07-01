# @algorithm @lc id=1349 lang=python3 
# @title check-if-it-is-a-straight-line


from en.Python3.mod.preImport import *
# @test([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])=true
# @test([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])=false
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        i, j = 0, 0
        def distance_check(point1: List[int], point2: List[int]):
            ratio = (point2[0] - point1[0]) / (point2[1] - point1[1])
            return ratio

        if len(coordinates) == 2:
            return True

        ratio = distance_check(coordinates[0], coordinates[1])

        for i in coordinates[1:]:
            if ratio != distance_check(coordinates[0], i):
                return False
        return True

