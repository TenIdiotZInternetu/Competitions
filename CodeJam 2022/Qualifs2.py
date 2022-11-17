T = int(input())

for t in range(T):
    print("Case #" + str(t + 1) + ":", end="")
    printers = []

    for i in range(3):
        printers.append(input().split())

        for j in range(4):
            printers[i][j] = int(printers[i][j])


    c = min((printers[0][0], printers[1][0], printers[2][0]))
    m = min((printers[0][1], printers[1][1], printers[2][1]))
    y = min((printers[0][2], printers[1][2], printers[2][2]))
    k = min((printers[0][3], printers[1][3], printers[2][3]))

    out = [c, m, y, k]

    if sum(out) < 1000000: 
        print(" IMPOSSIBLE")
        continue

    temp = out

    for i in range(4):
        
        temp[i] = 0

        if sum(temp) < 1000000:
            diff = 1000000 - sum(temp)
            temp[i] = diff
            break

    for ink in temp:
        print(" " + str(ink), end="")

    print("")

