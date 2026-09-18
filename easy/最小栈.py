class MinStack(object):

    def __init__(self):
        self.st = []
        self.minq = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.st.append(value)
        # 这里的判别要带等号，因为如果重复压入两个相同最小值，
        # 如果只保留一个压入，后续弹栈时弹出一个最小值，
        # 当前最小值就改变了，但是实际上，还有一个最小值没有弹出，
        # 最小值没有随着minq的这次出栈而改变。
        if not self.minq or self.minq[-1] >= value:
            self.minq.append(value)

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()
        if self.minq[-1] == self.st[-1]:
            self.minq.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minq[-1]

