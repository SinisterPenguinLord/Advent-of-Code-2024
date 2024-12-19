ds = [(1,0),(0,1),(-1,0),(0,-1)]

with open("input18.txt") as file:
    t=0
    text = file.read().split("\n")
    miss = text[1024:]
    text = text[:1024]
    gr = {}
    mins = {}
    for x in range(71):
        for y in range(71):
            if (str(x)+","+str(y)) in text:
                gr[(x,y)] = "#"
            else:
                gr[(x,y)] = "."
    mds = []
    for m in miss:
        z = m.split(",")
        gr[(int(z[0]),int(z[1]))] = '#'
        mins = {}
        mins[(0,0)] = 0
        mins[(70,70)] = 10000
        vis = [(0, (0,0))]
        while len(vis) > 0:
            (d,(x,y)) = vis.pop(0)
            for (dx,dy) in ds:
                (nx,ny) = (x+dx,y+dy)
                if nx in range(71) and ny in range(71):
                    if gr[(nx,ny)] == ".":
                        if (nx,ny) not in mins or mins[(nx,ny)] > d + 1:
                            mins[(nx,ny)] = d + 1
                            vis.append((d+1,(nx,ny)))
            vis = sorted(vis)
        
        t = mins[(70,70)]
        if not t in mds:
            print(m,t)
            mds.append(t)
            