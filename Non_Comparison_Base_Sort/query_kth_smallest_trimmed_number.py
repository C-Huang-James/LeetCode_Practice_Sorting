from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        """
        Given a list of strings `nums` and a list of queries, each query consists of two integers `k` and `trim`. 
        The function returns the index of the k-th smallest number in `nums` after trimming each number to its last `trim` digits.
        """
        # Create a list of tuples containing the trimmed numbers and their original indices
        
        ans = []
        for (k, trim) in queries:
            trimmed_nums = [[int(num[-trim:]), i] for i ,num in enumerate(nums)]
            trimmed_nums.sort()
            # print(trimmed_nums)
            ans.append(trimmed_nums[k-1][1])

        return ans

    

# Example usage:
if __name__ == "__main__":
    nums = ["102","473","251","814"]
    queries = [[1,1],[2,3],[4,2],[1,2]]
    solution = Solution()
    result = solution.smallestTrimmedNumbers(nums, queries)
    print(result)  # Output: [2, 2, 1, 0]