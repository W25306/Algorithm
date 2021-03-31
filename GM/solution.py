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
    for idx, item in enumerate(a):
        if idx == 0 or idx == len(a) - 1:
            continue
        if max(item, left[idx - 1], right[idx + 1]) != item:
            answer += 1
        else:
            print(item)
    return answer


def solution_23(routes):
    """
    Problem : 프로그래머스 단속카메라
    Algorithm : Greedy
    """
    answer = 1
    routes.sort()
    gate = routes[0][1]
    for i, item in enumerate(routes[:-1]):
        if gate > item[1]:
            gate = item[1]
        if gate < routes[i + 1][0]:
            answer += 1
            gate = routes[i + 1][1]

    return answer


def solution_24(n, words):
    """
    Problem : 프로그래머스 영어끝말잇기
    """
    collection = set()
    steps = 0
    for step in range(0, len(words), n):
        steps += 1
        for i in range(step, step + n):
            if i > 0 and words[i - 1][-1] != words[i][0]:
                return [i % n + 1, steps]
            if words[i] in collection:
                return [i % n + 1, steps]
            else:
                collection.add(words[i])
    return [0, 0]


def solution_25(n):
    NOTATION = '0123'

    def change(N):
        q, r = divmod(N, 3)
        n = NOTATION[r]
        return change(q) + n if q else n

    answer = change(n)
    result = 0
    for i, s in enumerate(answer):
        result += 3 ** i * int(s)
    return result


def solution(N, stages):
    """
    Problem : 프로그래머스 실패율
    Algorithm : heap, collections.Counter
    """
    from collections import Counter
    import heapq
    answer = []
    heap = []
    count = Counter(stages)
    length = len(stages)

    for i in range(1, N + 1):
        if length < 1:
            heapq.heappush(heap, (0, i))
        else:
            heapq.heappush(heap, (-(count[i] / length), i))
        length -= count[i]
    while heap:
        answer.append(heapq.heappop(heap)[1])
    return answer


def solution(genres, plays):
    class album:
        def __init__(self, g, p):
            self.genre = g
            self.play = p

    from collections import defaultdict
    answer = []
    library = defaultdict(album)
    for genre, play in zip(genres, plays):
        print(genre, play)
        if genre in library:
            pass
        else:
            newAlbum = album(genre, play)
            if not answer:
                answer.append(newAlbum)
            else:
                pass

    return answer


def sol1():
    from collections import deque
    n = int(input())
    queue = deque(maxlen=2)
    for i in range(n):
        time = input().split(" ~ ")
        if not queue:
            queue.appendleft(time[0])
            queue.append(time[1])
        else:
            left = queue.popleft()
            queue.appendleft(max(left, time[0]))
            right = queue.pop()
            queue.append(min(right, time[1]))
    print(queue.popleft() + " ~ " + queue.pop())


def sol2():
    count = [0, 0, 0, 2, 3]
    for i in range(5, 51):
        count.append(count[i - 1] + count[i - 2])
    n = int(input())
    path = input().split("0")
    answer = 0
    if path[0] == "11":
        answer += 1
    for p in path:
        answer += count[len(p)]
    print(answer)


def sol22():
    n = int(input())
    path = input()
    stack = [0]
    answer = 0
    while stack:
        item = stack.pop()
        if item == n - 1:
            answer += 1
        if item + 1 < n:
            if path[item + 1] == '1':
                stack.append(item + 1)
        if item + 2 < n:
            if path[item + 2] == '1':
                stack.append(item + 2)
    print(answer)


def sol3():
    def split(arr, left, right, top, bottom):
        sumValue = 0
        for i in range(top, bottom):
            sumValue += sum(arr[i][left:right])
        return sumValue

    n = int(input())
    room = []
    total = 0
    for i in range(n):
        temp = list(map(int, input()))
        total += sum(temp)
        room.append(temp)
    stage = [total]
    for i in range(2, n + 1):
        temp = 0
        for col in range(n - i + 1):
            for row in range(n - i + 1):
                if split(room, row, row + i, col, col + i) == i ** 2:
                    temp += 1
        stage.append(temp)
    print("total:", sum(stage))
    for i, v in enumerate(stage):
        if v:
            print("size[" + str(i + 1) + "]: " + str(v))


def sol4():
    import heapq
    preference = list(map(float, input().split(" ")))
    col, row = list(map(int, input().split(" ")))
    library = []
    subject = []
    for c in range(col):
        library.append(input())
    for c in range(col):
        subject.append(input())
    heapY = []
    heapO = []
    for i, col in enumerate(zip(library, subject)):
        for j, row in enumerate(zip(col[0], col[1])):
            if row[0] == 'Y':
                heapq.heappush(heapY,
                               ((-preference[ord(row[1]) - 65], i, j), (row[1], preference[ord(row[1]) - 65], i, j)))
            if row[0] == 'O':
                heapq.heappush(heapO,
                               ((-preference[ord(row[1]) - 65], i, j), (row[1], preference[ord(row[1]) - 65], i, j)))
    while heapY:
        out = heapq.heappop(heapY)[1]
        print(out[0], out[1], out[2], out[3])
    while heapO:
        out = heapq.heappop(heapO)[1]
        print(out[0], out[1], out[2], out[3])


def sol5():
    row, col = list(map(int, input().split(" ")))
    room = []
    answer = 0

    for c in range(col):
        room.append(list(map(str, input())))
    startPoint = []
    for r in range(row):
        if room[0][r] == 'c':
            startPoint.append([0, r, 0])
    answer = []
    for start in startPoint:
        check = [[False] * row for _ in range(col)]
        stack = [start]
        while stack:
            item = stack.pop()
            check[item[0]][item[1]] = True
            if item[0] == col - 1:
                answer.append(item[2])
                continue
            if room[item[0] + 1][item[1]] == '.':
                stack.append([item[0] + 1, item[1], item[2]])
            if room[item[0] + 1][item[1]] == 'x':
                if item[1] < row - 1:
                    if not check[item[0]][item[1] + 1]:
                        stack.append([item[0], item[1] + 1, item[2] + 1])
                if item[1] > 0:
                    if not check[item[0]][item[1] - 1]:
                        stack.append([item[0], item[1] - 1, item[2] + 1])
    print(min(answer))


def sol6():
    row, col = list(map(int, input().split(" ")))
    room = []
    for c in range(col):
        room.append(list(map(int, input().split(" "))))
    for c in range(col):
        for r in range(row):
            if c == 0 and r == 0:
                continue
            elif c == 0:
                room[c][r] += room[c][r - 1]
            elif r == 0:
                room[c][r] += room[c - 1][r]
            else:
                room[c][r] += max(room[c][r - 1], room[c - 1][r])
    print(room[col - 1][row - 1])


def solu1():
    from datetime import datetime
    num, sumTime = input().split(" ")
    musicList = []
    count = 0
    startPoint = 0
    pt = datetime.strptime(sumTime, '%H:%M:%S')
    sumTime = pt.second + pt.minute * 60 + pt.hour * 3600
    for _ in range(int(num)):
        minute, second = map(int, input().split(":"))
        musicList.append(minute * 60 + second)
    for i, v in enumerate(musicList):
        sumValue = 0
        cnt = 0
        idx = i
        while sumValue < sumTime and idx < int(num):
            sumValue += musicList[idx]
            cnt += 1
            idx += 1
        if cnt > count:
            count = cnt
            startPoint = i + 1
    print(count, startPoint)


def solu2():
    num = int(input())
    city_list = []
    city_set = set()
    parent = {}
    rank = {}

    def make(v):
        parent[v] = v
        rank[v] = 0

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        r1 = find(a)
        r2 = find(b)

        if r1 != r2:
            if rank[r1] > rank[r2]:
                parent[r2] = r1
            else:
                parent[r1] = r2

                # if rank[r1] == rank[r2]:
                #     rank[r2] += 1

    def check(city_set, city_list):
        cost = 0
        for c in city_set:
            make(c)
        edges = city_list
        edges.sort(key=lambda x: int(x[2]))
        for edge in edges:
            a, b, v = edge
            if find(a) != find(b):
                union(a, b)
                cost += int(v)
        return cost

    for _ in range(num):
        path = input().split()
        city_list.append(path)
        city_set.add(path[0])
        city_set.add(path[1])
    result = check(city_set, city_list)
    print(result)


def solu3():
    from collections import deque
    def find(a, queue):
        for i, v in enumerate(board[a]):
            if v:
                queue.append(i)

    num, ask = map(int, input().split())
    board = [[False] * num for _ in range(num)]
    board = board
    for _ in range(num - 1):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = True
    for _ in range(ask):
        a, b = map(int, input().split())
        queue = deque([a-1])
        found = False
        while queue:
            item = queue.popleft()
            if item == b - 1:
                found = True
                break
            find(item, queue)
        print('yes') if found else print('no')


def solu4():
    length = int(input())
    index_list = []
    for _ in range(length):
        index_list.append(input())
    num = int(input())
    for _ in range(num):
        type = input()
        cnt = 0
        for item in index_list:
            if type in item:
                cnt += 1
        print(cnt)


def solu42():
    from collections import defaultdict
    from itertools import combinations
    length = int(input())
    index_list = defaultdict(int)
    for _ in range(length):
        key = input()
        for i in range(2, min(len(key) + 1, 21)):
            combi = combinations(key, i)
            for item in combi:
                item = "".join(item)
                val = index_list[item]
                if val == 0:
                    index_list[item] = 1
                else:
                    index_list[item] = val + 1
    count = int(input())
    for _ in range(count):
        print(index_list[input()])

def solu43():
    def search(pattern, text):
        m = len(pattern)
        n = len(text)
        lps = [0]*m
        compute(pattern, lps)
        i = 0
        j = 0
        while i<n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            elif pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i +=1
            if j == m:
                return True
        return False

    def compute(pattern, lps):
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

    def find(parent, pattern):
        parentSize = len(parent)
        patternSize = len(pattern)
        parentHash = 0
        patternHash = 0
        power = 1
        for i in range(parentSize-patternSize+1):
            if i == 0:
                for j in range(patternSize):
                    parentHash += ord(parent[patternSize - 1-j])*power
                    patternHash += ord(pattern[patternSize-1-j])*power
                    if j < patternSize-1:
                        power *=2
            else:
                parentHash = 2*(parentHash-ord(parent[i-1])*power)+ord(parent[patternSize-1+i])
            if parentHash == patternHash:
                found = True
                for j in range(patternSize):
                    if parent[i+j]!=pattern[j]:
                        found = False
                        break
                if found:
                    return True
                else:
                    return False

    def getPartialMatch(N):
        m = len(N)

        pi = [0] * m
        begin = 1
        matched = 0
        while begin + matched < m:
            if N[begin + matched] == N[matched]:
                matched += 1
                pi[begin + matched - 1] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - pi[matched - 1]
                    matched = pi[matched - 1]
        return pi

    def kmpSearch(H, N):
        n = len(H)

        m = len(N)
        ret = []
        pi = getPartialMatch(N)
        begin = 0
        matched = 0
        while begin <= n - m:
            if matched < m and H[begin + matched] == N[matched]:
                matched += 1
                if matched == m:
                    ret.append(begin)
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - pi[matched - 1]
                    matched = pi[matched - 1]
        return ret

    length = int(input())
    index_list = []
    for _ in range(length):
        index_list.append(input())
    num = int(input())
    for _ in range(num):
        key = input()
        cnt = 0
        for item in index_list:
            if kmpSearch(item, key):
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    solu43()
    # test = ["classic", "pop", "classic", "classic", "pop"]
    # N = [500, 600, 150, 800, 2500]
    # print(solution(test,N))
