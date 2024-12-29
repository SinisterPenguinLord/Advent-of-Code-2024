from itertools import permutations

g1 = [['7','8','9'],['4','5','6'],['1','2','3'],['#','0','A']]
g2 = [['#','^','A'],['<','v','>']]

d1 = {}
d2 = {}

move = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}

for x in range(len(g1)):
    for y in range(len(g1[x])):
        d1[g1[x][y]] = (x,y)

for x in range(len(g2)):
    for y in range(len(g2[x])):
        d2[g2[x][y]] = (x,y)

b = {}

def length(inp,de,d):
    if (inp,de) in b:
        return b[(inp,de)]
    if de == 0:
        return len(inp)
    (x,y) = d['A']
    l = 0
    for c in inp:
        nl = ""
        (nx, ny) = d[c]
        dx = nx - x
        dy = ny - y
        n = 0
        e = 0
        s = 0
        w = 0
        if dx < 0:
            n = (-dx)
        else:
            s = dx
        if dy < 0:
            w = (-dy)
        else:
            e = dy
        nl += ">"*e + "^"*n + "<"*w + "v"*s

        news = set(permutations(nl))
        good = []
        for new in news:
            new = "".join(new)
            f = False
            p = (x,y)
            for ch in new:
                px = move[ch]
                p = (p[0]+px[0],p[1]+px[1])
                if d['#'] == p:
                    f = True
            if not f:
                good.append(length(new+"A",de-1,d2))
        l += min(good)
        (x,y) = (nx,ny)
    b[(inp,de)] = l
    return l



with open("input21.txt") as file:
    t = 0
    text = file.read().split("\n")
    for l in text:
        t += length(l,26,d1)*int(l[:-1])
    print(t)
