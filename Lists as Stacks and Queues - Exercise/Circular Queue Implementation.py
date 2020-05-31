# Circular Queue implementation in Python


class MyCircularQueue(object):

    def __init__(self, k):
        self.maxlen = k
        self.currlen = 0
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    # Insert an element into the circular queue
    def enQueue(self, value):

        if self.isFull():
            return False

        tail = (self.tail + 1) % self.maxlen
        self.queue[tail] = value
        self.tail = tail
        self.currlen += 1
        if self.currlen == 1:
            self.head = 0

        return True

    # Delete an element from the circular queue
    def deQueue(self):
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.maxlen
        self.currlen -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1

        return True

    # Get the front item from the queue
    def Front(self):
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    # Get the last item from the queue
    def Rear(self):
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    # Checks whether the circular queue is empty or not
    def isEmpty(self):
        return self.currlen == 0

    # Checks whether the circular queue is full or not
    def isFull(self):
        return self.currlen == self.maxlen

    # Display the queue
    def Display(self):
        for i in range(self.head, self.tail):
            print(self.queue[i], end=" ")


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
obj.enQueue(5)
print("Initial array")
print(obj.Display())

print("After removing an element")
obj.deQueue()
obj.Display()
obj.enQueue('fuck')
obj.Display()