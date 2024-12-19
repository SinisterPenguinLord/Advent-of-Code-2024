with open("input5.txt") as file:
    t=0
    text = file.read().split("\n\n")
    text[0] = text[0].split("\n")
    rules = []
    for r in text[0]:
        r = r.split("|")
        rules.append((int(r[0]),int(r[1])))
    
    text[1] = text[1].split("\n")
    updas = []
    for r in text[1]:
        r=r.split(",")
        updas.append(list(map(int, r)))
        
    
    for up in updas:
        u = []
        for x in up:
            z=0
            while z < len(u):
                if (x,u[z]) in rules:
                    break
                z+=1
            u.insert(z,x)
        print((u,up))
        if u != up:    
            t += u[len(up)//2]
    print(t)