n = int(input())
data = [int(i) for i in input().split()]
out = ""

for i in range(7, n + 1):
    span = sorted(data[i - 7:i])
    out += str(span[3]) + " "

print(out.strip())
