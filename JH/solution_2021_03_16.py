   
def solution(arr):
    answer = [0,0]
    length = len(arr)
    
    def recur(x,y,n):
        first = arr[x][y]
        for i in range(x, x+ n):
            for j in range(y,y+n):
                if arr[i][j] != first:
                    n = n//2
                    recur(x,y,n)
                    recur(x,y+n,n)
                    recur(x+n,y,n)
                    recur(x+n,y+n,n)
                    return
        answer[first] += 1
    recur(0,0,length)
    return answer
