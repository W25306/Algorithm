def testfunc(n,m,arr):
    result = 0
    answer = []
    for i in range(n):
        answer.append(min(arr[i]))
    
    return max(answer)

print(testfunc(3,3,[[3,1,2],[4,1,4],[2,2,2]]))
print(testfunc(2,4,[[7,3,1,8],[3,3,3,4]]))

def testfunc2(n,k):
    result = 0

    while n != 1:
        if n % k != 0:
            n -= 1
            result += 1
        else:
            n = n // k
            result += 1
    
    return result

print(testfunc2(25,5),testfunc2(25,3),testfunc2(27,3))
