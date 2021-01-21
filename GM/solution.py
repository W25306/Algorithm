# coding=utf-8
import math

def solution(name):
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

if __name__ == '__main__':
    name = "HAZ"
    print(solution(name))
