with open("input8.txt") as file:
    t=0
    text = file.read().split("\n")
    ants = {}
    for x in range(len(text)):
        for y in range(len(text[0])):
            if text[x][y] != ".":
                try:
                    ants[text[x][y]] = ants[text[x][y]] + [(x,y)]
                except:
                    ants[text[x][y]] = [(x,y)]
    nods = set()
    for ant in ants:
        poss = ants[ant]
        for x in range(1,len(poss)):
            for y in range(x):
                d = (poss[x][0]-poss[y][0], poss[x][1]-poss[y][1])
                pos = (poss[x][0]-50*d[0],poss[x][1]-50*d[1])
                for _ in range(100):
                    if pos[0] in range(len(text)) and pos[1] in range(len(text[0])):
                        nods.add(pos)
                    pos = (pos[0]+d[0],pos[1]+d[1])
                    
    print(len(nods))
                    
                
