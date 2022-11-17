T = int(input())

for t in range(T):
    N = int(input())
    dice = input().split()

    for n in range(N):
        dice[n] = int(dice[n])

    dice = sorted(dice)
    skip = False
    j = 1

    for i in range(N):

        if dice[i] < j: continue
        else:
            highest = j
            j += 1
            

    print("Case #" + str(t + 1) + ":", highest)