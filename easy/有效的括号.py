# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

#定义一个括号组成的字符串数组：
strs=["()[]{}","([{}])","([)]"]

class Solution(object):
    def isValid(self, s):
        # 定义一个空列表
        stack1 = []
        # 定义一个字典
        brackets = {'(': ')', '{': '}', '[': ']'}
        # 遍历字符串
        for char in s:
        #   遇到左括号入栈
            if char in brackets:
                stack1.append(char)
        #   如果不在字典中，char必是右括号，先看栈是否为空，不为空则将顶层元素出栈并判断
            elif not stack1:
                return False
            else:
                top = stack1.pop()
                if brackets[top] != char:
                    return False
        #   最后判断栈是否为空
        return not stack1
#   测试
for s in strs:
#   新建一个solution对象
    so = Solution()
    print(so.isValid(s))




