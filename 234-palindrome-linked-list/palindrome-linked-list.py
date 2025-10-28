# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        
        prev = None
        slow = fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next


        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        
        while prev and head and prev != head:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next
        
        return True


        
        


