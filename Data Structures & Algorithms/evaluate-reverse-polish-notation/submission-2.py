class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = ('+', '-', '*', '/')

        res = []
        for t in tokens:
            if t in d:
                s = int(stack.pop())
                f = int(stack.pop())
                if t == "+":
                    stack.append(f+s)
                elif t == "-":
                    stack.append(f-s)
                elif t == "*":
                    stack.append(f*s)
                else:
                    stack.append(f/s)

            else:
                stack.append(int(t))

        return int(stack.pop())

        
        # result = [tokens[0]]
        # r = 2
        # l = 1

        # while r<len(tokens):
        #     result.append(tokens[r])
        #     result.append(tokens[l])
        #     l+=2
        #     r+=2
        #     result = "".join(result)
        #     result = str(eval(result))
        #     result = [result]

        # return int(result[0])


        