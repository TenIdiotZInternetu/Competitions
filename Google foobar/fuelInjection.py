import random

def solution(n):
    num = int(n)
    count = 0

    while num > 1:
        if num == 3:
            count += 2
            return count
            
        if num % 2 == 0: num //= 2
        else:
            if ((num - 1) // 2) % 2 == 0: num -= 1
            else: num += 1

        count += 1

    return count

print(solution("934653653456035656356024654564576573562576205734056023453576523980465027563450324756043765345673"))

for i in range(100):
    print(i, "->", solution(str(i)))

par = ""

for i in range(309):
    par += str(random.randint(0, 9))

print(solution(par))