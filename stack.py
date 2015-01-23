class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
st = Stack()
st.push(10)
st.push(20)
print st.pop()
print st.data