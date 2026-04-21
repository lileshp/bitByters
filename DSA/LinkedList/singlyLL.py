class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    #insert at start
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    #insert at End
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def insert_inbetween(self,target_data,data):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print(f"Target Node {target_data} not Found")

    def display(self):
        if not self.head:
            print("LL is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} -> ",end="")
            temp = temp.next
        print("None")

    #deletion
    def delete_begining(self):
        # LL empty
        if not self.head:
            print("LL is empty")
            return
        print(f"Deleted node is {self.head.data}")
        self.head = self.head.next
    
    def delete_end(self):
        if not self.head:
            print("LL is empty")
            return
        if not self.head.next:
            print("Deleted node is {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print(f"Deleted node is {temp.next.data}")
        temp.next = None
        
    def delete_value(self, key):
        if not self.head:
            print("LL is empty")
            return
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("KEy not found in LL")
            return
        prev.next = temp.next
        print(f"Deleted Node {key}")

    def search(self,key):
        if not self.head:
            print("LL is empty")
            return
        pos = 0
        temp = self.head
        while temp:
            if temp.data == key:
                return f"{key} Key found at {pos} position"
            temp = temp.next
            pos += 1
        return f"{key} Key not found"
    
    #Length of the LL
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        

LL = LinkedList()
LL.insert_at_start(10)
LL.insert_at_end(20)
LL.insert_at_start(30)
LL.insert_at_start(60)
LL.insert_at_start(50)
LL.insert_inbetween(10,40)
LL.display()
LL.reverse()
LL.display()
print(LL.search(10))
LL.delete_value(30)
LL.display()
LL.delete_begining()
LL.display()
LL.delete_end()
LL.display()
LL.insert_inbetween(10,2000)
LL.display()

#Dangling Pointer
'''
Always check 3 conditions
    1. if LL is empty
    2. if there is only one node in LL
    3. if deleted node is head
'''
