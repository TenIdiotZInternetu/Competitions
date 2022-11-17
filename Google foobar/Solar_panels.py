def solution(area):
    out = []
    
    while area > 0:
        multiple = 1
    
        while 1:
            print(multiple, " ** 2 = ", multiple ** 2)
            if multiple ** 2 > area:
                out.append((multiple - 1) ** 2)
                area -= (multiple - 1) ** 2
                break
        
            multiple += 1
          
    return out

print(solution(15324))