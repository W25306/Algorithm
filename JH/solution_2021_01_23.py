def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion):
        if i != j:
            return i

def solution(answers):
    student1 = []
    student2 = []
    student3 = []
    s1_count = 0
    s2_count = 0
    s3_count = 0
    
    for i in range(len(answers)):
        student1.append(i % 5 + 1)
    for i in range(len(answers)):
        if i % 2 == 0:
            student2.append(2)
        else:
            if (8 * i + i) %8 == 1:
                student2.append(1) 
            elif (8 * i + i) %8 == 3:
                student2.append(3)
            elif (8 * i + i) %8 == 5:
                student2.append(4)
            else:
                student2.append(5)
        
    for i in range(len(answers)):
        if i % 10 == 0 or i% 10 == 1:
            student3.append(3)
        elif i % 10 == 2 or i% 10 == 3:
            student3.append(1)
        elif i % 10 == 4 or i% 10 == 5:
            student3.append(2)
        elif i % 10 == 6 or i% 10 == 7:
            student3.append(4)
        else:
            student3.append(5)
    
    for i in range(len(answers)):
        if student1[i] == answers[i]:
            s1_count = s1_count + 1
        if student2[i] == answers[i]:
            s2_count = s2_count + 1
        if student3[i] == answers[i]:
            s3_count = s3_count + 1
    
    a = [s1_count,s2_count,s3_count]
    answer = []
    max_number = max(a)
    for i in range(len(a)):
        if a[i] == max_number:
            answer.append(i + 1)
    return answer