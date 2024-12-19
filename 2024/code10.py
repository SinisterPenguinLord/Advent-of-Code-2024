def test(x,y,h):
    if x in range(len(g)) and y in range(len(g[0])):
        if g[x][y] == h:
            if h == 9:
                return 1
            return test(x+1,y,h+1) + test(x-1,y,h+1) + test(x,y+1,h+1) + test(x,y-1,h+1)
    return 0
    

with open("input10.txt") as file:
    t=0
    text = file.read().split("\n")
    g = []
    for r in text:
        row = []
        for c in r:
            try:
                row.append(int(c))
            except:
                row.append(".")
        g.append(row)
    for x in range(len(g)):
        for y in range(len(g[0])):
            a = test(x,y,0)
            t += a
            #if len(a) > 0:
             #   print(x,y,a)
    print(t)
            
    
    
    