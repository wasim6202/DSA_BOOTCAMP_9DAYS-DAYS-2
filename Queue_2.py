class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Queue contents:")
        index = self.front
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print()

# Test the Queue
queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()

print("Front item is", queue.get_front())
print("Rear item is", queue.get_rear())

print("Dequeued", queue.dequeue())
print("Dequeued", queue.dequeue())

queue.display()

queue.enqueue(6)
queue.enqueue(7)

queue.display()

print("Front item is", queue.get_front())
print("Rear item is", queue.get_rear())