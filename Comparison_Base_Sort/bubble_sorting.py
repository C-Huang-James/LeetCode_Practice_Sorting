from typing import List
# Bubble Sort Algorithm
# Time Complexity: O(n^2) in the worst case
# Space Complexity: O(1) since it sorts in place
# Best case: O(n) when the list is already sorted
# Stability: Bubble sort is a stable sorting algorithm

class Solution:
    def bubble_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that it is sorted via swapping adjacent elements until
        the entire lst is sorted.
        """
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    # Swap adjacent elements
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True          

machine = Solution()
lst = [5, 3, 8, 6, 2]
print("Before sorting:", lst)
machine.bubble_sort(lst)
print("After sorting:", lst)