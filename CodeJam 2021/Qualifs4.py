entry = input().split()
T = int(entry[0])
N = int(entry[1])

for t in range(T):
    L = list(range(1, N + 1))
    done = False
    memory = []

    while not done:
        done = True

        for i in range(N - 2):
            three = sorted((L[i], L[i + 1], L[i + 2]))
            question = "{0} {1} {2}".format(three[0], three[1], three[2])

            if question in memory:
                continue

            print(question, flush=True)
            answer = int(input())
            memory.append(question)

            if answer == L[i]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp
                done = False

            elif answer == L[i + 2]:
                temp = L[i + 2]
                L[i + 2] = L[i + 1]
                L[i + 1] = temp
                done = False

            print(L)

    res = ""

    for l in L:
        res += str(l) + " "

    print(res)
            
