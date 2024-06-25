class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Underflow: The squere is empty")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Overflow: The squere is full")
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__queue[0]


if __name__ == "__main__":
    queue2 = MyQueue(capacity=2)

    queue2.enqueue(1)

    queue2.enqueue(2)

    print(queue2.front())

    print(queue2.is_full())

    print(queue2.dequeue())

    print(queue2.dequeue())

    print(queue2.is_empty())

    print(queue2.is_empty())
