z = int(input())
n = input()
neg = False
substr = ""
i = 1

if n[0] == "-": neg = True

while i <= len(n) and not neg or i < len(n):
    new = str(int(n[-i]) + 1) if not neg else str(int(n[-i]) - 1)

    if int(new) >= z and not neg: new = "0"
    elif int(new) <  0 and neg: new = str(z - 1)

    substr = new + substr

    if (int(new) > 0 and not neg) or (int(new) < z - 1 and neg): break

    i += 1

n = n[:-i] + substr
if i > len(n): n = "1" + n

if neg and n[1] == "0":
    n = "-" + n[2:]

if n == "-": n = 0

print(n)

