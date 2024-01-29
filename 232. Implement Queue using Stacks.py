class MyQueue(object):

    def __init__(self):
        self.list = []
        self.list2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        while self.list:
            self.list2.append(self.list.pop())
        self.list.append(x)
        while self.list2:
            self.list.append(self.list2.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.list.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.list[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.list
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()