import itertools

def solution(num, req):
    arr = [i for i in range(num)]
    combs = list(itertools.combinations(arr, num - req + 1))
    out = [[] for i in range(num)]

    for i in range(len(combs)):
        for j in range(len(combs[0])):
            out[combs[i][j]].append(i)


    return out


print(solution(6, 5))
print(solution(5, 4))
print(solution(5, 3))
print(solution(5, 2))
print(solution(2, 1))
print(solution(4, 4))
print(solution(3, 2))