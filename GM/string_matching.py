
def simple_string_matching_algorithm(target, pattern):
    targetLength = len(target)
    patternLength = len(pattern)
    for s in range(targetLength-patternLength+1):
        if pattern == target[s:s+patternLength]:
            return True
    return False


def rabinkarp_matching_algorithm(target, pattern):
    targetLength = len(target)
    patternLength = len(pattern)
    patternHash = 0
    targetHash = 0
    power = 1

    for i in range(1, patternLength + 1):
        targetHash += ord(target[patternLength - i]) * power
        patternHash += ord(pattern[patternLength - i]) * power
        if i < patternLength:
            power *= 2

    for s in range(targetLength-patternLength+1):
        if patternHash == targetHash:
            if pattern == target[s:s+patternLength]:
                return True
        if s < targetLength - patternLength:
            targetHash = 2 * (targetHash - ord(target[s]) * power) + ord(target[patternLength + s])
    return False

def kmp_matching_algorithm(target, pattern):
    targetLength = len(target)
    patterLength = len(pattern)
    pi = getPi(pattern)
    q = 0
    for i in range(targetLength):
        while q > 0 and pattern[q] != target[i]:
            q = pi[q-1]
        if pattern[q] == target[i]:
            q += 1
        if q == patterLength:
            return True
    return False

def getPi(pattern):
    patternLength = len(pattern)
    pi = [0]
    k = 0
    for q in range(1, patternLength):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k]
        if pattern[k] == pattern[q]:
            k += 1
        pi.append(k)
    return pi
if __name__ == '__main__':
    target = "ABC ABCDAB ABCDABCDABDE"
    pattern = "ABC"
    print(simple_string_matching_algorithm(target, pattern))
    print(rabinkarp_matching_algorithm(target,pattern))
    print(kmp_matching_algorithm(target,pattern))

