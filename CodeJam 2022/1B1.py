T = int(input())

for t in range(T):
    N = int(input())
    vals = [int(i) for i in input().split()]

    max = 0
    count = 0

    i = 0
    j = 1

    while vals:
        if vals[0] <= vals[-1]:
            if vals[0] >= max: 
                max = vals[0]
                count += 1

            vals.pop(0)
            continue

        if vals[0] > vals[-1]:
            if vals[-1] >= max:
                 max = vals[-1]
                 count += 1

            vals.pop(-1)
            continue

    print("Case #" + str(t + 1) + ":", count)

        

