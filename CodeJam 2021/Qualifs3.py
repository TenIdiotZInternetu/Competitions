T = int(input())
out = []

for t in range(T):
    entry = input().split()
    N = int(entry[0])
    C = int(entry[1])
    L = ""

    if C < N - 1:
        out.append("IMPOSSIBLE")
        continue

    base = list(range(1, N + 1))
    cd = base
    print(base)
    sum = 0
    sindex = 0
    eindex = N

    for i in base:
        sum += i

    if C > sum - 1:
        out.append("IMPOSSIBLE")
        continue
    
    for i in range(1, N + 1):
        print(cd[-i], C)
        if C - cd[-i] >= cd[-i] - 2 and C - cd[-i] >= 0:
            C -= cd[-i]
            pre = base[:sindex]
            seg = base[sindex:eindex]
            rest = base[eindex:]
            seg.reverse()

            print(i, ":", pre)
            print(i, ":", seg)
            print(i, ":", rest)

            base = pre + seg + rest
        else:
            C -= 1
            
        if i % 2 == 0: sindex += 1
        else: eindex -= 1

    for l in base:
        L += str(l) + " "

    out.append(L)

for i in range(len(out)):
    print("Case #{0}: {1}".format(i + 1, out[i]))

