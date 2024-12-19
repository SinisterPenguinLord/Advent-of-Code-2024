def printgr():
    for y in range(len(text)):
        for x in range(len(text[y])):
            if gr[(x,y)] == '#':
                print("#",end = "")
            elif (x,y) in vised:
                print("O",end = "")
            else:
                print(" ",end = "")
        print()
        
def printp():
    for y in range(len(text)):
        for x in range(len(text[y])):
            if gr[(x,y)] == '#':
                print("#",end = "")
            elif (x,y) in vised:
                print("O",end = "")
            else:
                print(" ",end = "")
        print()

with open("input16.txt") as file:
    t=0
    text = file.read().split("\n")
    gr = {}
    ds = [(0,-1),(1,0),(0,1),(-1,0)]
    ps = [0, 1000, 2000, 1000]
    vised = set()
    for y in range(len(text)):
        for x in range(len(text[y])):
            if text[y][x] == '#':
                gr[(x,y)] = '#'
            else:
                gr[(x,y)] = [[1000000,[]],[1000000,[]],[1000000,[]],[1000000,[]]]
                if text[y][x] == 'S':
                    gr[(x,y)] = [[1000,[]],[0,[]],[1000,[]],[2000,[]]]
                    vis = [(0,1,x,y),(1000,0,x,y),(1000,2,x,y),(2000,3,x,y)]
                elif text[y][x] == 'E':
                    end = (x,y)
    vised = set((vis[0][2],vis[0][3]))
    while len(vis) > 0:
        [dis, d, x, y] = vis.pop(0)
        gr[(x,y)][d][0] = dis
        x1 = x +ds[d][0]
        y1 = y +ds[d][1]
        if gr[(x1,y1)] != '#':
            if gr[(x1,y1)][d][0] > dis + 1:
                gr[(x1,y1)][d] = [dis + 1, [(x,y,d)]]
                vis.append((dis+1,d,x1,y1))
            elif gr[(x1,y1)][d][0] == dis + 1:
                gr[(x1,y1)][d][1].append((x,y,d))
        
        if gr[(x,y)][(d+1)%4][0] > dis + 1000:
            gr[(x,y)][(d+1)%4] = [dis + 1000, [(x,y,d)]]
            vis.append((dis+1000,(d+1)%4,x,y))
        elif gr[(x,y)][(d+1)%4][0] == dis + 1000: 
            gr[(x,y)][(d+1)%4][1].append((x,y,d))
            
        if gr[(x,y)][(d-1)%4][0] > dis + 1000:
            gr[(x,y)][(d-1)%4] = [dis + 1000, [(x,y,d)]]
            vis.append((dis+1000,(d-1)%4,x,y))
        elif gr[(x,y)][(d-1)%4][0] == dis + 1000: 
            gr[(x,y)][(d-1)%4][1].append((x,y,d))
            
        vis = sorted(vis)
            
        #     if gr[(x,y)][d][0] > dis + 
        #     for z in range(4):
        #         if gr[(x,y)][(z+d)%4][0] > dis + ps[z] + 1:
        #             gr[(x,y)][(z+d)%4] = [dis + ps[z] + 1,[(ox,oy,(d+z)%4)]]
        #             vis.append((dis+ps[z]+1,(z+d)%4,x,y))
        #         elif gr[(x,y)][(z+d)%4][0] == dis +ps[z] + 1:
        #             gr[(x,y)][(z+d)%4][1].append((ox,oy,(d+z)%4))
        
        
        
        # vis = sorted(vis)
#        print(vis)
#        input()
    vised = {end}
    vis = []
    t = min(gr[end])[0]
    for p in gr[end]:
        if p[0] == t:
            vis += p[1]
    while len(vis) > 0:
        (x,y,d) = vis.pop()
        vised.add((x,y))
        vis += gr[(x,y)][d][1]
#        print((x,y,d))
    print(len(vised))
        
        
        
    # (x,y) = end
    # print(len(vised))
    # printp()
    