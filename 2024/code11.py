import time
start_time = time.time()
def up(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        c = str(n)
        return [int(c[:len(c)//2]),int(c[len(c)//2:])]        
    return [n*2024]

def rup(n,bs):
    if bs == 0:
        d[(n,bs)] = 1
    else:
        s = up(n)
        t = 0
        for x in s:
            try:
                t += d[(x,bs-1)]
            except:
                rup(x,bs-1)
                t += d[(x,bs-1)]
        d[(n,bs)] = t
                
            
                
                
    

with open("input11.txt") as file:
    t=0
    ss = []
    d = {}
    text = file.read().split(" ")
    for s in text:
        ss.append(int(s))
    fs = []
    
    for s in ss:
        print(s)
        rup(s,75)
        t += d[(s,75)]
    
    print(t)
    
print("--- %s seconds ---" % (time.time() - start_time))