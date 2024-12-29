with open("input23.txt") as file:
    text = file.read().split("\n")
    cs = {}
    vs = set()
    for l in text:
        (a,b) = l.split("-")
        vs.add(a)
        vs.add(b)
        if a in cs:
            cs[a].add(b)
        else:
            cs[a] = {b}
        if b in cs:
            cs[b].add(a)
        else:
            cs[b] = {a}


def max(vs,ads):
    global m
    if len(vs) > m[0]:
        m = (len(vs),vs)
    for v in ads:
        if not v in vs:
            if len(vs.union({v})) + len(ads.intersection(cs[v])) > m[0]:
                max(vs.union({v}),ads.intersection(cs[v]))

print(len(vs))
m = (0,set())
for v in vs:
    print(v, len(cs[v]))
    max({v},cs[v])
    print(m)

print(",".join(sorted(list(m[1]))))



'''
    trs = []
    t = 0
    for a in cs:
        for b in cs[a]:
            for c in cs[b]:
                if a in cs[c]:
                    if not sorted([a,b,c]) in trs:
                        trs.append(sorted([a,b,c]))'''

m = 0


'''
    trs = sorted(trs)
    print(len(trs))
    fors = []
    for a in range(len(trs)):
        for b in range(a):
            for c in range(b):
                s = set(trs[a]+trs[b]+trs[c])
                if len(s) == 4:
                    fors.append(sorted(list(s)))
    print(len(fors))
    print(fors[:20])'''