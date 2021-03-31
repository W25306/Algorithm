import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            c = a + (b * 2)
            heapq.heappush(scoville,c)
            count += 1
    return count
