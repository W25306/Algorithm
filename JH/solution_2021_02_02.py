def solution(skill, skill_trees):
    answer = 0
    skills = []
    # 스킬 순서 인덱스 변환
    for i,p in enumerate(skill):
        skills.append(i)
    for i in range(len(skill_trees)):
        a = skill_trees[i]
        # 스킬트리중 하나 가지고온다.
        trees = []
        check = True
        # 스킬트리 인덱스를 변환하여 배열에 넣어줌
        for j in range(len(a)):
            if a[j] in skill:
                trees.append(skill.index(a[j]))
        if len(trees) == 1:
            if trees[0] != 0:
                check = False
        # 만일 스킬트리의 해당하는 길이가 1이고 첫번째가 아니라면 스킬트리에 어긋남 False로 변환        
        else:
            for j in range(0,len(trees)-1):
                # 2개 이상일때 처음이 0이 아니면 false
                if trees[0] != 0:
                    check = False
                    break
                # 만일 다음 스킬트리의 값이 1더한게 아니라면 false    
                elif trees[j+1] != trees[j] + 1:
                    check = False(21)
                    break
                # 혹은 만약 다음 스킬트리의 값이 더 작다면 false
                elif trees[j] > trees[j+1]:
                    check= False
                    print(32)
                    break
        # check가 True 일때 만 값 증가
        if check:
            answer += 1
              
    return answer