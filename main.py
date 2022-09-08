n = int(input())
arr = []
result = []

for _ in range(n) :
    a = input()
    arr.append(a)

for ps in arr :
    if ps.count("(") != ps.count(")") :
        result.append("NO")
        continue
    while True :
        if ps[0] == ")" :
            result.append("NO")
            break
        ps = ps.replace("(", "", 1)
        ps = ps.replace(")", "", 1)

        if len(ps) == 0 :
            result.append("YES")
            break

for i in result :
    print(i)