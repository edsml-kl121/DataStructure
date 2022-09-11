def balancedBrackets(string):
    # Write your code here.
    matching = {"{": "}", "(": ")", "[": "]"}
    close_bracket = ["}", ")", "]"]
    open_bracket = ["{", "(", "["]
    current_stack = []
    if len(string) == 0:
        return True
    for i in range(0, len(string)):
        if string[0] in close_bracket:
            return False
        print(string[i])
        if string[i] in close_bracket:
            print('hi')
            print(current_stack)
            print('hi', current_stack[-1])
            if matching[current_stack[-1]] == string[i]:
                current_stack.pop()
            else:
              return False
        else:
          current_stack.append(string[i])
              # pass
        
    if current_stack == []:
        return True
    else:
        return False

# string = "([])(){}(())()()"
string = "()[]{}{"

print(balancedBrackets(string))