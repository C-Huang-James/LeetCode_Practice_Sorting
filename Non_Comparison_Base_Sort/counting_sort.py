from typing import List
# Counting Sort
# Time Complexity: O(n + k) where n is the number of elements in the input list and k is the range of the input
# Space Complexity: O(k) where k is the range of the input
# Stability: Counting Sort is a stable sort.
# Counting sort is a non-comparison based sorting algorithm that is efficient for sorting integers within a known range.

class Solution:
    def counting_sort(self, lst) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K.
        """
        K = max(lst)
        counts = [0] * (K+1)
        for elem in lst:
            counts[elem] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0]*len(lst)

        for elem in lst:
            sorted_lst[counts[elem]] = elem
            # since we have placed an item in index counts[elem], we need to
            # increment counts[elem] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[elem] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(len(lst)):
            lst[i] = sorted_lst[i]

        return lst


class SolutionModify:
    def counting_sort(self, lst: List[int]) -> None:
        """
        Sorts a list of integers (handles shifting of integers to range 0 to K)
        """
        shift = min(lst)
        K = max(lst) - shift
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem - shift] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            sorted_lst[counts[elem - shift]] = elem
            # since we have placed an item in index counts[elem], we need to
            # increment counts[elem] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[elem - shift] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
        return lst