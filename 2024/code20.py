cheats = {}
for x in range(-20,21):
    for y in range(-20,21):
        if abs(x) + abs(y) <= 20:
            cheats[(x,y)] = abs(x) + abs(y)

with open("input20.txt") as file:
    t=0
    text = file.read().split("\n")
    for x in range(len(text)):
        for y in range(len(text[x])):
            if text[x][y] == "S":
                star = (x,y)
            elif text[x][y] == "E":
                end = (x,y)
    mins = {star:0}
    vis = [(0,star)]
    ds = [(1,0),(-1,0),(0,1),(0,-1)]
    while len(vis) > 0:
        (d,(x,y)) = vis.pop(0)
        for (dx,dy) in ds:
            nx = x + dx
            ny = y + dy
            if text[nx][ny] != "#":
                if ((nx,ny) not in mins) or ((nx,ny) in mins and mins[(nx,ny)] > d + 1):
                    mins[(nx,ny)] = d + 1
                    vis.append((d+1,(nx,ny)))

    skips = {}

    for x in range(len(text)):
        for y in range(len(text[0])):
            if text[x][y] == '#':
                skips[(x,y)] = (0,0,0,0)
            else:
                skip = []
                for (dx,dy) in cheats:
                    nx = x + dx
                    ny = y + dy
                    if nx in range(len(text)) and ny in range(len(text[0])) and text[nx][ny] != '#':
                        s = mins[(x,y)]-mins[(nx,ny)]-cheats[(dx,dy)]
                        if s >= 100:
                            t += 1
                        skip.append(s)
                skips[(x,y)] = skip

    print(t)



