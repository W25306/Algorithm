def solution(arr):
    answer = []
    small = arr.index(min(arr))
    arr.pop(small)
    if len(arr) == 0:
        return [-1]
    else:
        return arr
    return answer

def solution(n, m):
    def gcd(n,m):
        if m == 0:
            return n
        else:
            return gcd(m, n % m)  
    answer = [gcd(n,m),(n*m) / gcd(n,m)]
    return answer

def solution(num):
    count = 0
    while num != 1:
        if count > 500:
            return -1
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
            
    return count

def solution(x):
    answer = True
    c_x = str(x)
    sum = 0
    for i in range(len(c_x)):
        sum += int(c_x[i])
    if x % sum == 0:
        return True
    else:
        return False
    return answer

def solution(d, budget):
    d = sorted(d)
    count = 0
    for i in range(len(d)-1):
        if budget > d[i+1] or budget == d[i+1]:
            budget -= d[i]
            count +=1
            print(d[i],d[i+1],budget)
        else:
            break
    if budget >= d[-1]:
        count+=1
    print(budget)
    return count

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,10,-1]]
    l_loc = [3,0]
    r_loc = [3,2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l_loc = [int(i/3),0]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r_loc = [int(i/3)-1,2]
        else:
            if i == 0:
                loc = [3,1]
            else:
                loc = [int(i/3),1]
            l_dist = (abs(loc[0] - l_loc[0]) + abs(loc[1] - l_loc[1]) ** 2) ** 0.5
            
            r_dist = (abs(loc[1] - r_loc[1]) + abs(loc[0] - r_loc[0])) ** 0.5
            l_dist = round(l_dist,2)
            r_dist = round(r_dist,2)
            print(l_loc,r_loc,loc,l_dist,r_dist)
            if r_dist > l_dist:
                answer += 'L'
                l_loc = loc
            elif r_dist < l_dist:
                answer += 'R'
                r_loc = loc
            elif l_dist == r_dist:
                print(1)
                if hand == 'right':
                    answer += 'R'
                    r_loc = loc
                else:
                    answer += 'L'
                    l_loc = loc
    return answer