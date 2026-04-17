class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        # 10 6 9 3 + -11 * / * 17 + 5 + 
        #  t
        
        # stack = [10,]
        # op2 = 5
        # op1 = 13
        # result = 

        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                result = 0
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    result = op1 + op2
                    stack.append(result)

                elif token == "*":
                    result = op1 * op2
                    stack.append(result)

                elif token == "/":
                    result = op1 / op2
                    stack.append(int(result))

                elif token == "-":
                    result = op1 - op2
                    stack.append(result)
            
        return stack.pop()