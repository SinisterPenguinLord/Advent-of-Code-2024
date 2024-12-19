ds = ([-1,0],[0,1],[1,0],[0,-1])

with open("input6.txt") as file:
    t=0
    text = file.read().split("\n")
    d = 0
    obs = set()
    vis = set()
    for x in range(len(text)):
        for y in range(len(text[x])):
            if text[x][y] == "#":
                obs.add((x,y))
            if text[x][y] == "^":
                pos = (x,y)
    pos0 = pos
    while pos[0] in range(len(text)) and pos[1] in range(len(text[0])):
        nex = (pos[0] + ds[d][0],pos[1] + ds[d][1])
        if nex in obs:
            d = (d+1)%4
        else:
            vis.add(pos)
            pos = nex
            
    vi = vis        
    for o in vi:
        pos = pos0
        d = 0
        vis = {}
        while pos[0] in range(len(text)) and pos[1] in range(len(text[0])):
            nex = (pos[0] + ds[d][0],pos[1] + ds[d][1])
            if nex in obs or nex == o:
                d = (d+1)%4
            else:
                try:
                    vis.update({pos:vis[pos]+1})
                except:
                    vis[pos] = 1
                if vis[pos] == 5:
                    t += 1
                    break
                pos = nex
            
    print(t)
    