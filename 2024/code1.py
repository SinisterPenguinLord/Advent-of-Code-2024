with open("input1.txt") as file:
    t=0
    text = file.read().split("\n")
    for x in range(len(text)):
        text[x] = text[x].split("   ")
    (a,b) = ([],[])
    for row in text:
        a.append(int(row[0]))
        b.append(int(row[1]))
        
    for x in range(len(a)):
        t += a[x]*b.count(a[x])
    print(t)