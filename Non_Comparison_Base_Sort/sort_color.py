from counting_sort import Solution as CountingSortSolution
from typing import List


machine = CountingSortSolution()
lst = [2, 0, 2, 1, 1, 0]
machine.counting_sort(lst)
print(lst)  # Output: [0, 0, 1, 1, 2, 2]
