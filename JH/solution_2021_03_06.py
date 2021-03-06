def solution(dirs):
    answer = 0
    start = [0,0]
    stack = []
    
    keyword = ['U','D','R','L']
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    for i in dirs:
        idx = keyword.index(i)
        prev_start = start
        nx = start[0] + dx[idx]
        ny = start[1] + dy[idx]
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        if stack.count([[nx,ny],prev_start]) != 0 or stack.count([prev_start,[nx,ny]]) != 0:
            start = [nx,ny]
            continue
        # print(stack.count([[nx,ny],prev_start]))
        start = [nx,ny]

        stack.append([start,prev_start])
    return len(stack)
