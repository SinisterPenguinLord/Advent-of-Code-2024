import time
start_time = time.time()

with open("input9.txt") as file:
    t=0
    text = file.read()
    mem = {}
    n = 0
    d = True
    e = [(0,0)]
    datas = {}
    x = 0
    for elem in text:
        if d:
            datas[n] = ((x,int(elem)))
            n += 1
            x += int(elem)
            d = False
        else:
            e.append((x,int(elem)))
            x += int(elem)
            d = True
    
    for x in range(len(datas)-1,-1,-1):
        (p,l) = datas[x]
        b = True
        for y in range(len(e)):
            (pe,le) = e[y]
            if pe >= p:
                break
            if l <= le:
                e[y] = (e[y][0]+l,e[y][1]-l)
                b = False
                t += x*sum(range(pe,pe+l))
                break
        if b:
            
            t += x*sum(range(p,p+l))
    print(t)
    
print("--- %s seconds ---" % (time.time() - start_time))    
    
    # for elem in text:
    #     if d:
    #         d = False
    #         for x in range(int(elem)):
    #             mem.append(n)
    #         n += 1
            
    #     else:
    #         d = True
    #         for x in range(int(elem)):
    #             mem.append(-1)
                
    # for i in range(len(mem)):
    #     try:
    #         while mem[i] == -1:
    #             mem[i] = mem.pop(-1)
    #     except:
    #         break
        
    # for i in range(len(mem)):
    #     t += i*mem[i]
        
    # print(t)
            
            