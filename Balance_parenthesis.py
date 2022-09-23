s = input()

stack = []

for char in s:
    
    if len(stack) == 0:
        stack.append(char)
    else:
        
        if char == ')' and stack[-1]=="(":
            stack.pop()
        elif char == '}' and stack[-1]=="{":
            stack.pop()
        elif char == '[' and stack[-1]=="[":
            stack.pop()
        
        else:
            stack.append(char)
if stack:
    print("No")
else:
    print("Yes")