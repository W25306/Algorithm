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
    for x in range(len(citations), -1, -1):
        cnt = 0
        for item in citations:
            if item >= x:
                cnt += 1
        if cnt >= x >= len(citations) - cnt:
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

    def find(array, x1, x2, y1, y2):
        if x2 - x1 == 1:
            return 0, 0
        one = 0
        zero = 0
        sumOfValue = 0
        for item in array[y1:y2]:
            sumOfValue += sum(item[x1:x2])
        if sumOfValue == (x2 - x1) ** 2:
            one += (x2 - x1) ** 2 - 1
            return zero, one
        elif sumOfValue == 0:
            zero += (x2 - x1) ** 2 - 1
            return zero, one
        temp1 = find(array, x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
        temp2 = find(array, x1, (x1 + x2) // 2, (y1 + y2) // 2, y2)
        temp3 = find(array, (x1 + x2) // 2, x2, y1, (y1 + y2) // 2)
        temp4 = find(array, (x1 + x2) // 2, x2, (y1 + y2) // 2, y2)
        zero += temp1[0] + temp2[0] + temp3[0] + temp4[0]
        one += temp1[1] + temp2[1] + temp3[1] + temp4[1]
        return zero, one

    zero, one = find(arr, 0, len(arr), 0, len(arr))
    return [zeros - zero, ones - one]


def solution_09(board):
    def find(bo, i, j):
        length = 1
        range = 0
        for cnt in range(1, len(bo) - max(i, j)):
            checkRow = True
            for row in range(cnt):
                if not bo[i + cnt][j + row]:
                    checkRow = False
            checkMid = bo[i + cnt][j + cnt]
            checkCol = True
            for col in range(cnt):
                if not bo[i + col][j + cnt]:
                    checkCol = False
            if checkRow and checkCol and checkMid:
                length = cnt + 1
            else:
                break
        return length

    maxLength = 0
    for i, colum in enumerate(board):
        for j, row in enumerate(colum):
            if row:
                temp = find(board, i, j)
                if maxLength < temp:
                    maxLength = temp
    return maxLength ** 2


def solution_10(s):
    """
    Problem : 올바른 괄호
    Algorithm : Stack
    """
    stack = [s[0]]
    for item in s[1:]:
        if not stack:
            stack.append(item)
            continue
        top = stack[-1]
        if top == item:
            stack.append(item)
        else:
            if top != ')':
                stack.pop(-1)

    return not stack


def solution_11(n):
    """
    Problem : 다음 큰 숫자
    Algorithm : Implementation
    """

    def check(n):
        A = 0
        for i in bin(n)[2:]:
            if i == '1':
                A += 1
        return A

    cntN = check(n)
    for i in range(n + 1, 1000000):
        cntB = check(i)
        if cntN == cntB:
            return i
    return 1000000


def solution_12(n):
    """
    Problem : 숫자의 표현
    Algorithm : Implementation
    """
    answer = 0
    if n % 2:
        r = n // 2 + 1
    else:
        r = n // 2
    for i in range(1, r):
        j = i + 1
        sumValue = i
        while sumValue < n:
            sumValue = sum(range(i, j))
            if sumValue == n:
                answer += 1
            else:
                j += 1
    return answer + 1


def solution_13(land):
    """
    Problem : 땅따먹기
    Algorithm : DP
    """
    for i in range(1, len(land)):
        for y in range(4):
            land[i][y] += max(land[i - 1][:y] + land[i - 1][y + 1:])
    return max(land[-1])


def solution_14(A, B):
    """
    Problem : 최솟값 만들
    """
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a * b
    return answer


def solution_15(arr):
    """
    Problem : N개의 최소공배수
    """
    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)

    stone = arr[0]
    for i in range(1, len(arr)):
        stone = lcm(stone, arr[i])
    return stone


def solution_16(nums):
    """
    Problem : 프로그래머스 소수 만들기
    Algorithm : Combination, Prime Number
    """
    from itertools import combinations
    answer = 0

    def isPrime(a):
        if (a < 2):
            return False
        for i in range(2, a):
            if (a % i == 0):
                return False
        return True

    combi = combinations(nums, 3)
    for item in combi:
        if isPrime(sum(item)):
            answer += 1
    return answer


def solution_17(n):
    """
    Problem : 프로그래머스 점프와 순간 이동
    """
    ans = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans + 1


def solution_18(s):
    """
    Problem : 프로그래머스 튜플
    """
    answer = []
    s = s[2:-2]
    sp = s.split("},{")
    for item in sp:
        temp = item.split(",")
        answer.append(list(map(int, temp)))
    answer.sort(key=lambda x: len(x))
    result = []
    for item in answer:
        for x in item:
            if x not in result:
                result.append(x)
    return result


def solution_19(s):
    """
    Problem : 짝지어 제거하기
    Algorithm : Stack
    """
    stack = []
    for item in s:
        if len(stack) == 0:
            stack.append(item)
            continue
        top = stack[-1]
        if top == item:
            stack.pop()
        else:
            stack.append(item)
    return int(len(stack) == 0)


def solution_20(n, t, m, p):
    """
    Problem : 프로그래머스 n진수 게임
    Algorithm : Implementation
    """
    NOTATION = '0123456789ABCDEF'

    def change(N, K):
        q, r = divmod(N, K)
        n = NOTATION[r]
        return change(q, K) + n if q else n

    result = ""
    i = 0
    while True:
        result += change(i, n)
        if len(result) > t * m + (p - 1):
            break
        i += 1
    answer = result[p - 1:len(result):m]
    return answer[:t]


def solution_21(n, a, b):
    """
    Problem : 프로그래머스 예상 대진표
    Algorithm : Binary Search
    """
    def sol(s, e, a, b):
        if a <= (s + e) / 2 and b <= (s + e) / 2:  # Same Side
            if abs(a - b) == 1:
                return 1
            answer = sol(s, (s + e) // 2, a, b)
        elif a > (s + e) / 2 and b > (s + e) / 2:  # Same Side
            if abs(a - b) == 1:
                return 1
            answer = sol((s + e) // 2, e, a, b)
        else:  # Diff Side
            answer = math.log(e - s, 2)
        return answer

    return int(sol(0, n, a, b))

def solution_22(a):
    """
    Problem : 프로그래머스 풍선 터트리기
    Algorithm : DP
    """
    answer = 2
    l = a[0]
    left = [l]
    r = a[-1]
    right = [r]
    for item in a[1:]:
        if item < l:
            l = item
        left.append(l)
    for item in a[-2::-1]:
        if item < r:
            r = item
        right.append(r)
    right.reverse()
    for idx,item in enumerate(a):
        if idx == 0 or idx == len(a)-1:
            continue
        if max(item,left[idx-1],right[idx+1]) != item:
            answer += 1
        else:
            print(item)
    print(left)
    print(right)
    return answer

if __name__ == '__main__':
    test = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    print(solution(test))
