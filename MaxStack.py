class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        
        self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_elem_in = 0
        for index, elem in enumerate(self.stack):
            # print(index, elem)
            if elem[0] == self.peekMax():
                max_elem_in = index
        # print(max_elem_in, self.stack)
        
        prev_max_elem = self.stack[max_elem_in - 1][1]
        for after_max_in in range(max_elem_in + 1, len(self.stack)):
            elem = self.stack[after_max_in][0]
            if after_max_in == 1:
                self.stack[after_max_in] = (elem, elem)
            else:
                self.stack[after_max_in] = (elem, max(prev_max_elem, elem))
            prev_max_elem = self.stack[after_max_in][1]
        
                
        return self.stack.pop(max_elem_in)[1]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()