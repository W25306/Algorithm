def solution(s):
    answer = []
    remove_zero = 0
    change_count = 0
    i = 0
    while True:
        remove_zero += s.count('0')
        change_count += 1
        s = s.replace('0','')
        if s == '1':
            break
        n = len(s)
        string = ''
        while True:
            b = n % 2
            n = n // 2 
            string += str(b)
            if n == 1:
                string += str(n)
                break
    
        string = string[::-1]
        s = string
        i += 1
    print(s,remove_zero,change_count)
            
    return [change_count,remove_zero]