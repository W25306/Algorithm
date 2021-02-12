def testfunc_using_Greedy(n,m,k,arr):
    a = sorted(arr)
    large = a[-1]
    second_large = a[-2]
    
    count = int(m / (k + 1)) * k
    b = large * count + second_large * (m -count)
    print(b)

def testfunc_not_using_Greedy(n,m,k,arr):
    a = sorted(arr)
    large = a[-1]
    second_large = a[-2]
    
    ans = 0
    i = 0
    b = 0
    while True:
        if i == m:
            break
        if b < 3:
            ans += large
            b += 1
            i += 1
        else:
            b = 0
            ans += second_large
            i += 1
    print(ans)
    
#--------------------------------------- 
testfunc_not_using_Greedy(5,8,3,[2,4,5,4,6])
