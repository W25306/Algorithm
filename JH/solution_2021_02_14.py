def solution(number, k):
    answer = ''
    count = 0
    i = 0
    stack = []
    test = list(number)
    if len(list(set(number[-k:]))) == 1:
        return number[:len(number) - k]
    for a in number:
        while stack and stack[-1] < a and k > 0:
            stack.pop()
            k -= 1
        stack.append(a)
    return "".join(stack)
