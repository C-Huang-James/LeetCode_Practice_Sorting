from typing import List
# Heap Sort Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Stability: Unstable


class Solution:
    def heap_sort(self, lst: List[int]) -> None:
        """
        Mutates elements in lst by utilizing the heap data structure.
        """
        def max_heapify(heap_size, index):
            left, right = 2* index +1, 2*index +2
            largest = index
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                max_heapify(heap_size, largest)

        def print_heap(heap_size):
            """
            Visualizes the current state of the heap.
            """
            print("Heap:", lst[:heap_size])

        # Step 1: Build a max heap from the input list
        # This step we ensure each heap is in max heap order
        print("Building the max heap:")
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)
            print_heap(len(lst))  # Visualize the heap after each heapify

        # Step 2: Extract elements from the heap one by one
        print("\nSorting the heap:")
        for i in range(len(lst) - 1, 0, -1):
            # Swap the root (largest element) with the last element
            lst[i], lst[0] = lst[0], lst[i]
            print(f"After swapping root with element at index {i}: {lst}")

            # Reduce the heap size and restore the max heap property
            max_heapify(i, 0) 
            # since the first index is swapped with the last index
            # , we need to heapify from the first index again

            print_heap(i)  # Visualize the heap after each heapify



