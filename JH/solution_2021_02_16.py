def testfunc(n,moves):
    
    loc = [1,1]
    
    move_list = ['R','L','U','D']
    move_r_l = [1,-1,0,0]
    move_u_d = [0,0,-1,1]
    
    for move in moves:
        for i in range(len(move_list)):
            if move == move_list[i]:
                move_x = loc[0] + move_r_l[i]
                move_y = loc[1] + move_u_d[i]
        if move_x < 1 or move_x > n or move_y >n or move_y < 1:
            continue
        else:
            loc = [move_x,move_y]
    print(loc)    


testfunc(5,['R','R','R'])
testfunc(10,['R','R','D','U','L','D','D','L','R'])
