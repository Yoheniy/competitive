class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # Initialize the circular queue with 'k' elements set to 0
        self.front_pointer = 0  # The front pointer to the first element of the circular queue
        self.current_size = 0  # Current number of elements in the circular queue
        self.capacity = k  # Maximum capacity of the circular queue

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue. Return true if the operation is successful."""
        if self.isFull():
            # Return False if the queue is full
            return False
        # Calculate the index at which to insert the new value
        idx = (self.front_pointer + self.current_size) % self.capacity
        self.queue[idx] = value  # Insert the value
        self.current_size += 1  # Increment the size of the queue
        return True  # Return True on successful insertion

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue. Return true if the operation is successful."""
        if self.isEmpty():
            # Return False if the queue is empty
            return False
        # Increment the front_pointer as we remove the front element
        self.front_pointer = (self.front_pointer + 1) % self.capacity
        self.current_size -= 1  # Decrement the size of the queue
        return True  # Return True on successful deletion

    def Front(self) -> int:
        """Gets the front item from the queue. If the queue is empty, return -1."""
        if self.isEmpty():
            # If the queue is empty, return -1
            return -1
        # Otherwise, return the front element
        return self.queue[self.front_pointer]

    def Rear(self) -> int:
        """Gets the last item from the queue. If the queue is empty, return -1."""
        if self.isEmpty():
            return -1

        idx = (self.front_pointer + self.current_size - 1) % self.capacity
        return self.queue[idx]

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.capacity

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()