'''
Merge Two sorted LL and create a new merged sorted LL
    l1 = [1,2,4]
    l2 = [1,3,4]
    output = [1,1,2,3,4,4]

we will use a dummy node:
set tail pointer at dummy node
iterate till nodes in sorted LL (both)
    if l1.data <= l2.data
        tail.next = l1
        l1 = l1.next
    else
        tail.next = l2
        l2 = l2.next
    tail = tail.next
tail = [] #tail.data = 0, tail.next = None
    1 <= 1
        tailnext = l1
        l1 = l1.next
    
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def merge_two_sorted_ll(ll1, ll2):
    dummy = Node(0)
    tail = dummy
    
    while ll1 and ll2:
        if ll1.data <= ll2.data:
            tail.next = ll1
            ll1 = ll1.next
        else:
            tail.next = ll2
            ll2 = ll2.next
        tail = tail.next
    
    if ll1:
        tail.next = ll1
    elif ll2:
        tail.next = ll2

    return dummy.next

def display(head):
    while head:
        print(f"{head.data} ->", end=" ")
        head = head.next
    print("NULL")

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)
l1.next.next.next = Node(5)
l1.next.next.next.next = Node(15)
l1.next.next.next.next.next = Node(17)
l1.next.next.next.next.next.next = Node(27)
l2 = Node(3)
l2.next = Node(7)
l2.next.next = Node(8)
l2.next.next.next = Node(20)
# print(l1.next.data)
res = merge_two_sorted_ll(l1,l2)
# print(res)

display(res)

'''
Time Complexity= O(n+m)
Space complexity = O(1)

solve with without dummy
'''

'''
Home Work:
    1. complete code of CDLL:
        delete: start, end, by value code
    
    2. search another to solve merged sorted LL program

    3. Remove nth node of a Linked List from end of LL. 
        # 2 pointer
'''

