with open("input13.txt") as file:
    t=0
    text = file.read().split("\n\n")
    for m in text:
        r = m.split("\n")
        r[0] = r[0].split(" ")
        r[1] = r[1].split(" ")
        r[2] = r[2].split(" ")
        a = (int(r[0][2][2:-1]),int(r[0][3][2:]))
        b = (int(r[1][2][2:-1]),int(r[1][3][2:]))
        tar = (int(r[2][1][2:-1])+10000000000000,int(r[2][2][2:])+10000000000000)
        
        det = a[0]*b[1] - b[0]*a[1]
        ka = b[1]*tar[0] - b[0]*tar[1]
        kb = -a[1]*tar[0] + a[0]*tar[1]
        
        #print(ka%det,kb%det, det)
        #print((ka*a[0]+kb*b[0])/det,tar[0])
        #print((ka*a[1]+kb*b[1])/det,tar[1])
        
        
        
        if ka/det == ka//det and kb/det == kb//det:
            ka = ka//det
            kb = kb//det
            if ka > 0 and kb > 0:
                t += 3* ka + kb
    print(t)
        
        
        #a*a[0] + b*b[0] = tar[0]
        #a*a[1] + b*b[1] = tar[1]
        
        #[a[0]   b[0]][a]  =  tar[0]
        #[a[1]   b[1]][b]  =  tar[1]
        
        #[a] =   1  [ b[1]  -b[0]][tar[0]]
        #[b] =  det [-a[1]   a[0]][tar[1]]
        
        
        