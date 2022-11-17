def solution(x, y):
    id = 1
    
    for i in range(x - 1):
        add = 2 + i
        id += add

    base = add

    for i in range(y - 1):
        add = base + i
        id += add

    return str(id)

print(solution(5, 10))