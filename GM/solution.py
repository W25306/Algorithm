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
    back = [right,left]

    for i in range(len(changeList)-1):
        A = changeList[i]
        B = changeList[i+1]
        back.append(2*A+(len(name)-B))
        back.append(A+2*(len(name)-B))

    A = changeList[-1]
    B = changeList[0]
    back.append(2 * A + (len(name) - B))
    back.append(A + 2*(len(name) - A))

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
    right = k +1
    result = ''
    def findMax(arr):
        maximum = '-1'
        idx = 0
        for i,x in enumerate(arr):
            if x > maximum:
                maximum = x
                idx = i
                if maximum == '9':break
        return idx+left, str(maximum)
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
        return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    closet = defaultdict(list)
    for item in clothes:
        closet[item[1]].append(item[0])
    result = 1
    for item in closet.keys():
        result *= getCombi(len(closet[item])+1,1)

    return result - 1


def solution(skill, skill_trees):
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

if __name__ == '__main__':
    test = "CBD"
    skill_trees = ["BACDE","CBADF","AECBD","BDA"]
    # print(solution('CBD', ['CAD']),0) #0
    # print(solution('CBD',['AEF', 'ZJW']),2)#2
    print(solution('REA',['REA', 'POA']),1)#1
    print(solution('CBDK',['CB', 'CXYB', 'BD', 'AECD', 'ABC', 'AEX', 'CDB', 'CBKD', 'IJCB', 'LMDK']),4)
    print(solution('BDC',['AAAABACA']),0)
    print(solution('CBD',['C', 'D', 'CB', 'BDA']),2)
