from typing import List

class Solution:

    def height_checker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for e, h in zip(expected, heights): 
            if e != h: 
                ans += 1
        return ans

machine = Solution()
lst = [5, 3, 8, 6, 2]
print(machine.height_checker(lst))

