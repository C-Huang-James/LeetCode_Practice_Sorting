from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums.sort()
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1 # if no key, default to 0
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # count.itmes() returns a list of tuples (key, value)
    # sorted by the second element of the tuple (value) in descending order
    # reverse is True to sort in descending order

    # return the first k elements of the sorted list
    return [item[0] for item in count[:k]] # list comprehension to extract the first k elements

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))  # Output: [1, 2]
