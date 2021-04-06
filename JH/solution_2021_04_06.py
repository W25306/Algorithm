def solution(gems):
    start, end = 0,0
    gem_num = len(set(gems))
    gem_dict = {gems[0]:1}
    result = [0,100001]
    while start < len(gems) and end < len(gems):
        if len(gem_dict) < gem_num:
            if end == len(gems) - 1:
                break
            end += 1
            if gem_dict.get(gems[end]) is None:
                gem_dict[gems[end]] = 1
            else:
                gem_dict[gems[end]] += 1
        else:
            if end - start < result[1] - result[0]:
                result = [start+1, end+1]
            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            start += 1
    return result
