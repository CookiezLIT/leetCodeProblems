
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 4 -> 2 -> 3

# 2 -> 3

# rev_item = (4,)
# next_item = (2, )
# next_item = (2, (4,))
# l=3
# rev_item = (2, (4, ))
# 

# 4
# 2 -> 4
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        node_1 = ListNode((l1.val + l2.val) % 10)
        first_node = node_1
        overflow = (l1.val + l2.val) > 9
        l1 = l1.next
        l2 = l2.next
        
        while True:
            aux_node = ListNode()
            if l1 and l2:
                aux_node.val = (l1.val + l2.val + overflow) % 10
                overflow = (l1.val + l2.val + overflow) > 9
                l1 = l1.next
                l2 = l2.next
                node_1.next = aux_node
                node_1 = aux_node
            elif l1:
                aux_node.val = (l1.val + overflow) % 10
                overflow = (l1.val + overflow) > 9
                l1 = l1.next
                node_1.next = aux_node
                node_1 = aux_node
            elif l2:
                aux_node.val = (l2.val + overflow) % 10
                overflow = (l2.val + overflow ) > 9
                l2 = l2.next
                node_1.next = aux_node
                node_1 = aux_node
            else:
                break
            

        if overflow:
            node_1.next = ListNode(1,None)

        return first_node
    
s=Solution()

l1 = ListNode(3, ListNode(7))
l2 = ListNode(9, ListNode(2))

a = s.addTwoNumbers(l1,l2)
print(a.val)
while a.next:
    a = a.next
    print(a.val)