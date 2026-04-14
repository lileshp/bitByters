class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_full(self):
        return self.rear == self.capacity - 1
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, element):
        if self.is_full():
            print("Queue is Overflow, we cannot insert element")
            return
        
        #First element insertion
        if self.front == -1:
            self.front += 1
        
        self.rear += 1
        self.queue[self.rear] = element
        print(f"Inserted an element : {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is underflow, we cannot remove any element")
            return
        element = self.queue[self.front]

        if self.rear == self.front:
            print("We removed last element")
            self.front = self.rear = -1
        else:
            self.front += 1
        
        return element
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty, there is no element in the queue")
        else:
            print(f"Queue: {self.queue}")

q = LinearQueue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.enqueue(40)