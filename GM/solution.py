# coding=utf-8
import math


def solution_01(name):
    """
    Problem : 프로그래머스 조이스틱
    Category : Greedy
    Result : Pass
    """
    changeList = []
    sum = 0
    if name[0] != 'A':
        sum += min(26 - (ord(name[0]) - ord('A')), ord(name[0]) - ord('A'))
        name = 'A' + name[1:]
    for i, s in enumerate(name):
        if s != 'A':
            changeList.append(i)
            sum += min(26 - (ord(s) - ord('A')), ord(s) - ord('A'))
    if len(changeList) == 0:
        return 0

    right = changeList[-1]
    left = len(name) - changeList[0]
    back = [right, left]

    for i in range(len(changeList) - 1):
        A = changeList[i]
        B = changeList[i + 1]
        back.append(2 * A + (len(name) - B))
        back.append(A + 2 * (len(name) - B))

    A = changeList[-1]
    B = changeList[0]
    back.append(2 * A + (len(name) - B))
    back.append(A + 2 * (len(name) - A))

    return sum + min(back)


def solution_02(num, k):
    """
    Problem : 프로그래머스 큰 수 만들기
    Category : Greedy
    Result : Pass
    Description : 숫자 크기 비교일 때는 0이나 9같은 끝 값 예외처리로 시간 단축하기
    """
    length = len(num)
    left = 0
    right = k + 1
    result = ''

    def findMax(arr):
        maximum = '-1'
        idx = 0
        for i, x in enumerate(arr):
            if x > maximum:
                maximum = x
                idx = i
                if maximum == '9': break
        return idx + left, str(maximum)

    k = length - k
    for i in range(k):
        idx, maxValue = findMax(num[left:right])
        left = idx + 1
        right += 1
        result += maxValue
    return result


from collections import deque


def solution_03(people, limit):
    """
    Problem : 프로그래머스 구명보트
    Category : Greedy, Time Complexity
    Result : Pass
    Description : List pop, remove : O(N) deque pop, popLeft : O(1)
    """
    people.sort(reverse=True)
    people = deque(people)
    result = 0
    while people:
        if len(people) < 2:
            result += 1
            break

        big = people.popleft()
        if big + people[-1] <= limit:
            people.pop()

        result += 1
    return int(result)


from collections import defaultdict


def solution_04(clothes):
    """
    Problem : 프로그래머스 위장
    Category : Math, Hash
    Result : Pass
    """

    def getCombi(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    closet = defaultdict(list)
    for item in clothes:
        closet[item[1]].append(item[0])
    result = 1
    for item in closet.keys():
        result *= getCombi(len(closet[item]) + 1, 1)

    return result - 1


def solution_05(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        arr = [skill_tree.find(char) for char in skill]
        for idx, ele in enumerate(arr[1:]):
            if ele == -1:
                continue

            # ele != -1
            if arr[idx] == -1 or arr[idx] > ele:
                break

        else:
            answer += 1

    return answer


def solution_06(n):
    answer = [[0] * i for i in range(1, n + 1)]
    x = -1
    y = 0
    s = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = s
            s += 1
    result = []
    for ans in answer:
        result += ans
    return result


def solution_07(citations):
    """
    Problem : 프로그래머스 H-Index
    Category : Sort
    Time : n^2
    """
    for x in range(len(citations),-1,-1):
        cnt = 0
        for item in citations:
            if item >= x:
                cnt+=1
        if cnt >= x >= len(citations)-cnt:
            return x
    return 0

def solution_08(arr):
    """
    Problem : 프로그래머스 쿼드압축 후 개수 세기
    Algorithm : Recursion
    """
    ones = 0
    for a in arr:
        ones += sum(a)
    zeros = len(arr) ** 2 - ones
    def find(array, x1, x2,y1,  y2):
        if x2 - x1 == 1:
            return 0,0
        one = 0
        zero = 0
        sumOfValue = 0
        for item in array[y1:y2]:
            sumOfValue += sum(item[x1:x2])
        if sumOfValue == (x2-x1)**2:
            one += (x2-x1)**2 - 1
            return zero, one
        elif sumOfValue == 0:
            zero += (x2-x1)**2 - 1
            return zero, one
        temp1 = find(array, x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
        temp2 = find(array, x1, (x1 + x2) // 2, (y1 + y2) // 2, y2)
        temp3 = find(array, (x1 + x2) // 2, x2, y1, (y1 + y2) // 2)
        temp4 = find(array, (x1 + x2) // 2, x2, (y1 + y2) // 2, y2)
        zero += temp1[0] + temp2[0] + temp3[0] + temp4[0]
        one += temp1[1] + temp2[1] + temp3[1] + temp4[1]
        return zero, one

    zero, one = find(arr,0,len(arr),0,len(arr))
    return [zeros-zero,ones-one]

if __name__ == '__main__':
    test = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
