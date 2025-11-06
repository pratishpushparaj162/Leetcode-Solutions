# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.ll = head
        self.count =  0
        while head:
            self.count += 1
            head = head.next

    def getRandom(self) -> int:
        node = self.ll
        count = self.count
        p = 1/count
        while node:
            if random.random() <= p: return node.val
            node = node.next
            count -= 1
            p = 1/count


   
            

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
