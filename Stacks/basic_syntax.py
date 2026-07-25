class stack:
    def __init__(self):
        self._data = []

    def push(self,x):
        self._data.append(x)

    def pop(self):
        if self.is_empty():
            return("Cannot pop from empty stack")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            return("Cannot peek from empty stack")
        return self._data[-1]
    
    def is_empty(self):
            return len(self._data) == 0
    
    def size(self):
         return len(self._data)

s = stack()
s.push(10)
s.push(100)
s.push(20)
print(s._data)
s.pop()
s.peek()
print(s._data)
s.pop()
s.pop()
print(s._data)
print(s.is_empty())