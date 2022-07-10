# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        l1_num = self.getNumber(l1)
        l2_num = self.getNumber(l2)
        
        l3 = l1_num + l2_num
        
        l3_list = [int(i) for i in str(l3)]
                
        dummy = cur = ListNode()
        while l3_list:
            cur.next = ListNode(l3_list.pop())
            cur = cur.next
        
        return dummy.next
    
    def reverseList(self, l):
        prev = None
        curr = l
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def getNumber(self, l):
        nums = []
        curr = l
        while curr:
            nums.append(str(curr.val))
            curr = curr.next
        return(int("".join(nums)))
        