import time
start_time = time.time()

def findreg(x,y):
    vis = {(x,y)}
    return reg(x,y,text[x][y],vis)

def reg(x,y,n,vis):
    tests = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for t in tests:
        (x1,y1) = t
        if x1 in range(len(text)) and y1 in range(len(text[0])):
            if (not t in vis) and text[x1][y1] == n: 
                vis.add((x1,y1))
                vis.union(reg(x1,y1,n,vis))
    return vis

def perim(reg):
    t = 0
    for (x,y) in reg:
        c = 4
        tests = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for te in tests:
            (x1,y1) = te
            if x1 in range(len(text)) and y1 in range(len(text[0])):
                if te in reg:
                    c -= 1
        t += c
    return t

def sides(reg):
    t = 0
    for (x,y) in reg:
        u = (x-1,y) in reg
        ul = (x-1,y-1) in reg
        l = (x,y-1) in reg
        d = (x+1,y) in reg
        dr = (x+1,y+1) in reg
        r = (x,y+1) in reg
        if not u and not (l and not ul):
            t += 1
        if not l and not (u and not ul):
            t += 1
        if not d and not (r and not dr):
            t += 1
        if not r and not (d and not dr):
            t += 1
    return t
        
        

with open("input12.txt") as file:
    t=0
    text = file.read().split("\n")
    regs = []
    for x in range(len(text)):
        for y in range(len(text[0])):
            z = (findreg(x,y))
            if not z in regs:
                regs.append(z)
    for re in regs:
        t += len(re)*sides(re)
    print(t)


print("--- %s seconds ---" % (time.time() - start_time))