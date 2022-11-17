T = int(input())
out = []

for t in range(T):
    N = int(input())
    L = input().split()
    cost = 0

    for l in range(N):
        L[l] = int(L[l])

    for i in range(N - 1):
        j = L.index(min(L[i:]))
        #print("L =", L)
        #print("j =", j)

        pre = L[:i]
        seg = L[i:j + 1]
        rest = L[j + 1:]

        seg.reverse()
        L = pre + seg + rest
        cost += j - i + 1

    out.append(cost)

for i in range(len(out)):
    print("Case #{0}: {1}".format(i + 1, out[i]))



