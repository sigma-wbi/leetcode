class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        
        answer = True
        
        stack = []
        
        for s in s_list:
            if s == '[' or s == '(' or s == '{':
                stack.append(s)
            elif len(stack) != 0:
                if (s == ']' and stack[-1] == '[') or (s == '}' and stack[-1] == '{') or (s == ')' and stack[-1] == '('): 
                    stack.pop()
                # 닫는 괄호가 들어왔는데 바로 직전 괄호가 매칭이 안되면 false
                else:
                    answer = False
                    break
            else:
                answer = False
                break
                
        if len(stack) != 0:
            answer = False
            
        return answer