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


if __name__ == '__main__':
    print(solution("1924",2))
    print(solution("1231234",3))
    print(solution("4177252841",4))
