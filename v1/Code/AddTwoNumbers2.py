# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.getNumber(l1)
        l2 = self.getNumber(l2)
        
        l3_num = l1 + l2
        
        l3_list = [int(i) for i in str(l3_num)]
        
        dummy = cur = ListNode()
        while l3_list:
            cur.next = ListNode(l3_list.pop(0))
            cur = cur.next
        
        return dummy.next
              
    def getNumber(self, l):
        nums = []
        curr = l
        while curr:
            nums.append(str(curr.val))
            curr = curr.next
        return(int("".join(nums)))
        