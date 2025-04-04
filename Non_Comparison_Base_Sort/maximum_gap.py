from typing import List

def maximumGap(nums: List[int]) -> int:
    nums.sort()
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    return max_gap if len(nums) > 1 else 0


# Example usage:
if __name__ == "__main__":
    nums = [3, 6, 9, 1]
    print(maximumGap(nums))  # Output: 3 (the maximum gap is between 6 and 9)