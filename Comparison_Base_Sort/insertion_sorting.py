from typing import List

class Solution:
    def insertion_sort(self, lst: List[int]) -> None:
        """
        Mutates elements in lst by inserting out of place elements into appropriate
        index repeatedly until lst is sorted
        """
        for i in range(1, len(lst)):
            current_index = i

            while current_index > 0 and lst[current_index - 1] > lst[current_index]:
                # Swap elements that are out of order
                lst[current_index], lst[current_index - 1] = lst[current_index - 1], lst[current_index]
                current_index -= 1 # trace back to the previous index

machine = Solution()
lst = [5, 2, 4, 6, 1, 3]
print("Before sorting:", lst) # Output: [5, 2, 4, 6, 1, 3]
machine.insertion_sort(lst)
print("After sorting:", lst) # Output: [1, 2, 3, 4, 5, 6]