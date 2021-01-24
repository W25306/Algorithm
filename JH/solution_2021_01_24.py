def solution(array, commands):
 
    answer = []
    command_length = len(commands)
    for i in range(command_length):
        select_command = commands[i]
        slice_1, slice_2 = select_command[0] - 1, select_command[1]
        split_array = array[slice_1:slice_2]
        split_array = sorted(split_array)
        k_number = split_array[select_command[2]-1]
        answer.append(k_number)
    return answer


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    lost = list(set_lost)
    reserve = list(set_reserve)
    smallest = n - len(lost)
    answer = []
    for i in lost:
        if i - 1 in reserve and i not in answer:
            smallest = smallest + 1
            answer.append(i)
            reserve.remove(i-1)
            continue
        elif i + 1 in reserve and i not in answer:
            smallest = smallest + 1
            answer.append(i) 
            reserve.remove(i+1)
            print(i,answer,reserve)
            continue
            
    return smallest
