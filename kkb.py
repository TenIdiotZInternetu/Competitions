n = int(input())
commits = input().split()
out = ""
cindex = 0
used = []

for i in range(n):
    commits[i] = int(commits[i])

commits = sorted(commits)

for i in range(1, n + 1):
    while cindex < len(commits) -1 and commits[cindex] == commits[cindex - 1]:
        cindex += 1

    if cindex < len(commits):
        if i != int(commits[cindex]):
            out += str(i) + " "
        else: cindex += 1
    else:
        out += str(i) + " "

print(out.strip())