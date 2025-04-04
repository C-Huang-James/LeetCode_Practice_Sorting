# Bucket Sort Algorithm
# Time Complexity: O(n + k) (average case), O(n^2) (worst case)
# Space Complexity: O(n + k)
# where n is the number of elements in the input array and k is the number of buckets.
# Stability: Bucket sort is stable if the sorting algorithm used to sort the individual buckets is stable.
from typing import List


class Solution:
    def bucket_sort(self, lst: List[int], K) -> None:
        """
        Sorts a list of integers using K buckets
        """
        buckets = [[] for _ in range(K)]

        # place elements into buckets
        shift = min(lst)
        max_val = max(lst) - shift
        bucket_size = max(1, max_val / K)
        for i, elem in enumerate(lst):
            # same as K * lst[i] / max(lst)
            index = int((elem - shift) // bucket_size)
            # edge case for max value
            if index == K:
                # put the max value in the last bucket
                # can only be one max value in the array
                buckets[K - 1].append(elem)
            else:
                buckets[index].append(elem)

        # sort individual buckets
        for bucket in buckets:
            bucket.sort()

        # convert sorted buckets into final output
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(bucket)

        # common practice to mutate original array with sorted elements
        # perfectly fine to just return sorted_array instead
        for i in range(len(lst)):
            lst[i] = sorted_array[i]

        return lst
    

# Example usage
if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3, 5, 6]
    K = 3
    solution = Solution()
    solution.bucket_sort(arr, K)
    print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7]