from typing import List
# Selection Sort Algorithm
# Time complexity: O(n^2)
# Space complexity: O(1)
# Best case: O(n^2) when the list is already sorted
# Stability: Selection sort is not a stable sorting algorithm

class Solution:
    def selection_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index
        """
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                # Update minimum index
                if lst[j] < lst[min_index]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            lst[min_index], lst[i] = lst[i], lst[min_index]

machine = Solution()
lst = [64, 25, 12, 22, 11]
print("Original list:", lst)
machine.selection_sort(lst)
print("Sorted list:", lst)