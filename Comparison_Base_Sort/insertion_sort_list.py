from typing import List, Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ListNode(head: Optional[ListNode]) -> None:
    """Utility function to print the linked list."""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Create a dummy node to act as the sorted part of the list
        dummy = ListNode(0)
        current = head

        while current:
            # Extract the next node to process
            next_node = current.next

            # Find the correct position in the sorted part
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert the current node into the sorted part
            current.next = prev.next
            prev.next = current

            # Move to the next node
            current = next_node

            print("Prev : ", end="")
            print_ListNode(prev)  # Print the current node being processed
            # print("Dummy : ", end="")
            # print_ListNode(dummy)  # Print the current state of the sorted list
            print("Current : ", end="")
            print_ListNode(current)  # Print the current node being processed
            print("Next : ", end="")
            print_ListNode(next_node)
            print("------------------------------------------")

        return dummy.next
    
    def insertionSortList_Best(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        node = ListNode(0)
        curr= node
        arr.sort()
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return node.next

# Create the linked list
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(7)
head.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next = ListNode(6)


print_ListNode(head)

machine = Solution()
sorted_head = machine.insertionSortList(head)

print_ListNode(sorted_head)