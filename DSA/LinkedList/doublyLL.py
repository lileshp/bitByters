class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DobulyLinkedList:
    def __init__(self):
        self.head = None
    
    #Insertion
    def insert_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
            print(f"Inserted {data} after {target} Node.")
        else:
            print(f"Target {target} not found in LL")

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <->",end=" ")
            temp = temp.next
        print("None")

    #DELETION
dll = DobulyLinkedList()
dll.insert_start(50)
dll.insert_start(40)
dll.insert_end(20)
dll.insert_end(10)
dll.insert_start(30)
dll.display()