class Stack:
    def __init__(self, items = None, limit = 100):
        self.limit = limit
        if items is None:
            items = []
        self.items =list(items)

    def isEmpty(self):
        return len(self.items) == 0   

    def push(self, item):
        if not self.full():
            return self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items(-1)
        return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for index, value in enumerate(self.items):
            if value == target:
                return len(self.items) - (index +1)
        return -1
    
stk = Stack([1,2,3,4,5,6],10)
print(stk.full())
