# Least Significant Digit (LSD) Radix Sort.
# Running time: O(d*(n+k)), where d is the number of digits in the largest number, n is the number of elements in the list, and k is the range of the digits (0-9).
# Space complexity: O(n+k), where n is the number of elements in the list and k is the range of the digits (0-9).
# Stability: Stable.

from typing import List

class Solution:
    def counting_sort(self, lst: List[int], place_val: int, K: int = 10) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K
        """
        # intitialize count array of size K (0 ~ 9)
        counts = [0] * K

        for elem in lst:
            digit = (elem // place_val) % 10
            counts[digit] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            digit = (elem // place_val) % 10
            sorted_lst[counts[digit]] = elem
            counts[digit] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
    
    def radix_sort(self, lst:List[int]) -> None:
        # shift the minimum value in lst to be 0
        shift = min(lst)
        lst[:] = [num - shift for num in lst]
        max_elem = max(lst)

        #apply the radix sort algorithm
        place_val = 1
        while place_val <= max_elem:
            self.counting_sort(lst, place_val)
            place_val *= 10

        # undo the original shift
        lst[:] = [num + shift for num in lst]