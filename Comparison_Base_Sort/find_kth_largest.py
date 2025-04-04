from typing import List

def findKthLargest(nums:List[int], k):
    def max_heapify(heap_size, index):
        left, right = 2*index+1, 2*index+2 
        largest = index
        if left < heap_size and nums[left]>nums[largest]:
            largest = left
        if right < heap_size and nums[right]>nums[largest]:
            largest = right
        if largest != index:
            nums[index], nums[largest] = nums[largest], nums[index]
            max_heapify(heap_size, largest)
    
    for i in range(len(nums)//2-1, -1,-1):
        max_heapify(len(nums), i) # max heapify the original array
    
    for i in range(len(nums)-1, 0, -1):
        # swap the largest to the end of the array and reduce size
        nums[0], nums[i] = nums[i], nums[0] 
        max_heapify(i, 0)
    
    return nums[-k]

lst = [3,2]
k = 2
print(findKthLargest(lst, k)) # Output: 5
            