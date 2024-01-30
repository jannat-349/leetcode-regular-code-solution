class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                if token == "+":
                    stack[-2] += stack[-1]
                elif token == "-":
                    stack[-2] -= stack[-1]
                elif token == "*":
                    stack[-2] *= stack[-1]
                else:
                    stack[-2] = int(float(stack[-2]) / stack[-1])
                
                stack.pop()
            else:
                stack.append(int(token))
            
            
        
        return stack.pop()