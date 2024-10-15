class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Deque is empty"

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return "Deque is empty"

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        return "Deque is empty"

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return "Deque is empty"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

# Test the Deque
deque = Deque()

print("Adding elements to the front:")
deque.add_front(1)
deque.add_front(2)
deque.add_front(3)
print(deque.display())

print("\nAdding elements to the rear:")
deque.add_rear(4)
deque.add_rear(5)
print(deque.display())

print("\nRemoving from front:", deque.remove_front())
print("Deque after removal:", deque.display())

print("\nRemoving from rear:", deque.remove_rear())
print("Deque after removal:", deque.display())

print("\nFront element:", deque.peek_front())
print("Rear element:", deque.peek_rear())

print("\nDeque size:", deque.size())

print("\nRemoving all elements:")
while not deque.is_empty():
    print("Removed:", deque.remove_front())

print("\nTrying to remove from empty deque:", deque.remove_front())