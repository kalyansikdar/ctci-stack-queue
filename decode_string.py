s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = '100[a]' return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

Algorithm: 
  1. push everything in a stack. 
  2. Pop from the stack till we encounter a number and push into another stack
  3. store the number into a variable
  4. Pop from the second stack till we encounter ']' and create a string, then multiply with the variable
  5. Put the new string into the first stack
  6. repeat

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list(s)
        print (stack)
        temp_stack = []

        while stack:
            ele = stack.pop()
            if ele.isnumeric():
                while stack and stack[-1].isnumeric():
                    ele += stack.pop()
                res = int(ele[::-1])
                y = ""
                while temp_stack:
                    ele2 = temp_stack.pop()
                    if ele2 != ']':
                        if ele2 != '[':
                            y += ele2
                    else:
                        break
              
                z = ""
                for _ in range(res): # z = y * res
                    z += y
                temp_stack.append(z)
                while temp_stack:
                    stack.append(temp_stack.pop())
            else:
                temp_stack.append(ele)

        temp_stack.reverse()
        return ("".join(temp_stack))
