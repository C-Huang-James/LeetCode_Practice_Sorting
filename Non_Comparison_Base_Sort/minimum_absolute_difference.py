from counting_sort import Solution as CountingSortSolution
from typing import List


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    # machine = CountingSortSolution()
    # machine.counting_sort(arr)
    arr.sort()
    result = []
    min_diff = float('inf')
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i - 1], arr[i]]]
        elif diff == min_diff:
            result.append([arr[i - 1], arr[i]])
    return result


# Example usage:
if __name__ == "__main__":
    arr = [4, 2, 1, 3]
    print(minimumAbsDifference(arr))  # Output: [[1, 2], [2, 3], [3, 4]]
