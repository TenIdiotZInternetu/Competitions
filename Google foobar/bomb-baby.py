def solution(M, F):
    m = int(M)
    f = int(F)
    order = 0

    if m % 2 == 0 and f % 2 == 0: return "impossible"
    
    while 1:
        if m == 1 and f == 1: return str(int(order))
        if m < 1 or f < 1: return "impossible"

        dif = abs(f - m)
        inc = -(-dif // min(f, m))

        if f > m: f -= m * inc
        elif m > f: m -= f * inc
        elif f == m: return "impossible"

        order += inc

print(solution("2", "1"))
print(solution("4", "7"))
print(solution("2", "2"))
print(solution("2", "4"))
print(solution("30", "13"))
print(solution("2012937612045012386551368413472461352432757345632752347426", "42356872356897985586778385637543835637549567325409"))