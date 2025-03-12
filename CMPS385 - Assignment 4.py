class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.tail = None  # Points to the last node in the queue

    def isEmpty(self):
        return self.tail is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node  # Circular reference for a single node
            self.tail = new_node
        else:
            new_node.next = self.tail.next  # New node points to front
            self.tail.next = new_node  # Old tail points to new node
            self.tail = new_node  # Update tail to new node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue.")
            return

        front_node = self.tail.next  # Front node (head)
        if self.tail == front_node:  # Only one node in queue
            self.tail = None
        else:
            self.tail.next = front_node.next  # Update tail's next to skip front node
        
        print(f"Dequeued: {front_node.data}")

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None
        return self.tail.next.data  # Front node is next of tail

# Example usage:
queue = CircularQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.getFront())  # Output: 10
queue.dequeue()
print("Front element after dequeue:", queue.getFront())  # Output: 20
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Should indicate that the queue is empty
