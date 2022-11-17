def solution(n, b):
    used = []

    while 1:
        y = "".join(sorted(str(n)))
        x = "".join(sorted(str(n), reverse=True))
        k = len(x)
        div = 0
        
        #print(x, y)
        
        for i in range(1, k + 1):
            digx = int(x[-i])
            digy = int(y[-i]) + div
            div = 0
        
            if digx < digy:
                digx += + b
                div = 1
        
            newdig = str(digx - digy)
        
            if i > 1: x = x[:-i] + newdig + x[-i + 1:]
            else: x = x[:-i] + newdig
                    
        n = x

        if n in used: return len(used) - used.index(n)
        else: used.append(n)

print(solution(1211, 10))