def reverseWordsInString(string):
    # Write your code here.
    words = []
    previous = 0
    for i in range(len(string)):
        if string[i] == " ":
            words.append(string[previous:i])
            previous = i
            
    for i in range(len(words)):
        words[i] = reversed(words[i], 0, len(words[i]) - 1)
    return " ".join(words)

def reversed(string, left=0, right=len(string)-1):
    string_arr = list(string)
    while left < right:
        string_arr[left], string_arr[right] = string_arr[right], string_arr[left]
        left += 1
        right -= 1
    return "".join(string_arr)