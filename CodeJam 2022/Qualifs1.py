T = int(input())

for t in range(T):
    R, C = input().split()
    R = int(R)
    C = int(C)
    
    out = []
    print("Case #" + str(t + 1) + ":")

    for i in range(R * 2 + 1):
        out.append([])
        

        for j in range(C * 2 + 1):
            if i < 2 and j < 2: 
                out[i].append('.')
                print('.', end="")
                continue

            # if i % 2 == 0 and j % 2 == 0: out[i].append('+')
            # if i % 2 == 0 and j % 2 != 0: out[i].append('-')
            # if i % 2 != 0 and j % 2 == 0: out[i].append('|')
            # if i % 2 != 0 and j % 2 != 0: out[i].append('.')

            if i % 2 == 0 and j % 2 == 0: print('+', end="")
            if i % 2 == 0 and j % 2 != 0: print('-', end="")
            if i % 2 != 0 and j % 2 == 0: print('|', end="")
            if i % 2 != 0 and j % 2 != 0: print('.', end="")

        print("")

    
    


