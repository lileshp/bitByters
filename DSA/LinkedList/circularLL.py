class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLL:
    def __init__(self):
        self.head = None

    #Insert
    def insert_at_start(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head
    
    def insert_after_node(self,target, data):
        if not self.head:
            print("LL is empty!!!")
            return
        
        temp = self.head
        while True:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Target {target} not found in LL")
    
    def display(self):
        if not self.head:
            print("LL is empty")
            return
        
        temp = self.head
        while True:
            print(f"{temp.data} ->",end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

    #DELETION

    def delete_start(self):
        if not self.head:
            print("LL is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("LL is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            prev.next = self.head

    def delete_value(self, key):
        if not self.head:
            print("LL is empty")
            return
        curr = self.head
        prev = None

        # if key == head
        if curr.data == key:
            self.delete_start()
            return

        while True:
            prev = curr
            curr = curr.next
            if curr == self.head:
                print("Key not found")
                break
            if curr.data == key:
                prev.next = curr.next
                return
        
cll = CircularSinglyLL()
cll.insert_at_start(20)
cll.insert_at_end(30)
cll.insert_after_node(20,40)
cll.display()
cll.delete_end()
cll.display()
cll.delete_start()
cll.display()
cll.insert_at_start(30)
cll.insert_at_start(20)
cll.insert_at_start(10)
cll.insert_at_start(100)
cll.display()