with open("input25.txt") as file:
    text = file.read().split("\n\n")
    ks = []
    ls = []
    for r in text:
        r = r.split("\n")
        n = ()
        tr = [*zip(*r)]
        for x in range(len(tr)):
            tr[x] = "".join(tr[x])
        for t in tr:
            n += (t.count('#')-1,)
        if r[0] == ".....":
            ks.append(n)
        else:
            ls.append(n)
    t = 0
    for k in ks:
        for l in ls:
            f = False
            for x in range(5):
                if k[x] + l[x] > 5:
                    f = True
            if not f:
                t += 1
    print(t)