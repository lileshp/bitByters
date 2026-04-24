class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDLL:
    def __init__(self):
        self.head = None
    
    def insert_begining(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = self.head.pre = new_node
            self.head = new_node
        print(f"{data} Inserted at beginning")
    
    def insert_at_end(self,data):
        if not self.head:
            self.insert_begining(data)
            return
        new_node = Node(data)
        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        print(f"{data} inserted at last of the CDLL")

    def insert_after(self, target, data):
        if not self.head: 
            print(f"LL is empty so we cannot find target {target} in LL")
            return
        curr = self.head
        while True:
            if curr.data == target:
                new_node = Node(data)
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node
                print(f"Inserted {data} after {target}")
                return
            curr = curr.next
            if curr == self.head:
                break
        print(f"Target {target} not found in CDLL")

    def display(self):
        if not self.head:
            print("LL is empty")
            return
        curr = self.head
        while True:
            print(f"{curr.data} <->",end=" ")
            curr = curr.next

            if curr == self.head:
                break
        print("HEAD")

cdll = CircularDLL()
cdll.insert_after(70,80)
cdll.insert_begining(20)
cdll.insert_begining(30)
cdll.display()
cdll.insert_at_end(50)
cdll.insert_begining(40)
cdll.insert_at_end(10)
cdll.display()
cdll.insert_after(50,60)
cdll.display()
cdll.insert_after(70,80)
cdll.display()
