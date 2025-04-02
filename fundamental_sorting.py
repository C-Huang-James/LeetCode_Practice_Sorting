from typing import List, Optional

class Solution:
    def __init__(self, lst: Optional[List[str]]=None):
        self.lst = lst

    def set_lst(self, lst: List[str]) -> None:
        """
        Sets the list of strings to be sorted
        """
        self.lst = lst

    def sort_by_length(self, lst:List[str]) -> None:
        """
        Sorts a list of strings by the length of each string
        """      
        self.lst = lst  
        self.lst.sort(key=lambda x: len(x)) # Note we can also do lst.sort(key=len)

machine = Solution()
lst = ["hello", "your", "above", "year", "alone", "friendly", "crazy"]
machine.sort_by_length(lst)
print(machine.lst) # Output: ['kiwi', 'pear', 'apple', 'banana']