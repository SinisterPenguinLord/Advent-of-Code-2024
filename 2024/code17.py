def search(l,u,p):
    global best
    i0 = -1
    for x in range(l,u+1,2**(51-3*p)):
        out = run(x)
        
        if out == prog:
            print(x)
            input()
        if i0 != prog[-p] and out[-p:] == prog[-p:]:
            nl = x
            i0 = out[-p]
        elif i0 == prog[-p] and out[-p] != prog[-p]:
            if p > best:
                print(x,out,p)
                best = p
            search(nl,x,p+1)
                        

            

best = 0
def run(a):
    regs = reg0.copy()
    regs[0] = a
    i = 0
    out = []
    while i in range(len(prog)):
        ins = prog[i]
        lop = prog[i+1]
        cop = c(lop,regs)
        i += 2
        if ins == 0:
            regs[0] = regs[0]//(2**cop)
        elif ins == 1:
            regs[1] = regs[1] ^ lop
        elif ins == 2:
            regs[1] = cop % 8
        elif ins == 3:
            if regs[0] != 0:
                i = lop
        elif ins == 4:
            regs[1] = regs[1] ^ regs[2]
        elif ins == 5:
            out.append((cop%8))
        elif ins == 6:
            regs[1] = regs[0]//(2**cop)
        elif ins == 7:
            regs[2] = regs[0]//(2**cop)
    return out
        

def run2(a):
    out = []
    while a != 0:
        bi = "0"*9+bin(a)[2:]
        if a % 8 == 0:
            out.append(4*int(bi[-10])+2*int(bi[-9])+int(bi[-8]))
            
        elif a % 8 == 1:
            out.append(4*int(bi[-9])+2*int(bi[-8])+(int(bi[-7]))^1)
            
        elif a % 8 == 2:
            out.append(4*int(bi[-8])+2*(int(bi[-7])^1)+int(bi[-6]))
            
        elif a % 8 == 3:
            out.append(4*int(bi[-7])+2*(int(bi[-6])^1)+(int(bi[-5])^1))
            
        elif a % 8 == 4:
            out.append(4*(int(bi[-6])^1)+2*int(bi[-5])+int(bi[-4]))
            
        elif a % 8 == 5:
            out.append(4*(int(bi[-5])^1)+2*int(bi[-4]))
            
        elif a % 8 == 6:
            out.append(4*(int(bi[-4])^1)+1)
            
        elif a % 8 == 7:
            out.append(0)
            
        a //= 8
    return out
            

# def rev(x,p):
#     if p == 17:
#         print(x)
            
#     t = bin(prog[-p])
#     nx = x.copy()
#     if nx[5+3*p] == "0":
#         nx[5+3*p] = int(t[2])
#     if nx[6+3*p] == "0":
#         nx[6+3*p] = int(t[1])
#     if nx[7+3*p] == "0":
#         nx[7+3*p] = int(t[0])
#     if nx[5+3*p:8+3*p] == [map(int, t)]:
#         rev(nx,p+1)
        
#     nx = x.copy()
#     if nx[5+3*p] == "0":
#         nx[5+3*p] = int(t[2])
#     if nx[6+3*p] == "0":
#         nx[6+3*p] = int(t[1])
#     if nx[7+3*p] == "0":
#         nx[7+3*p] = int(t[0])
#     if nx[5+3*p:8+3*p] == [map(int, t)]:
#         rev(nx,p+1)
        
    
    
def rev(x,p):
    #3digs are x[3*p],x[3*p+1],x[3*p+2]
    if p == len(prog):
        o = ""
        for i in range(48):
            o += str(x[i])
        print(int(o,2))
        print()
        return True
    
    if prog[15-p] == 4*x[3*p-7] + 2*x[3*p-6] + x[3*p-5]:
        nx = x.copy()
        nx[3*p] = 0
        nx[3*p+1] = 0
        nx[3*p+2] = 0
        rev(nx, p+1)
    
    if prog[15-p] == 4*x[3*p-6] + 2*x[3*p-5] + x[3*p-4]^1:
        nx = x.copy()
        nx[3*p] = 0
        nx[3*p+1] = 0
        nx[3*p+2] = 1
        rev(nx, p+1)
    
    if prog[15-p] == 4*x[3*p-5] + 2*(x[3*p-4]^1) + x[3*p-3]:
        nx = x.copy()
        nx[3*p] = 0
        nx[3*p+1] = 1
        nx[3*p+2] = 0
        rev(nx, p+1)
    
    if prog[15-p] == 4*x[3*p-4] + 2*(x[3*p-3]^1) + x[3*p-2]^1:
        nx = x.copy()
        nx[3*p] = 0
        nx[3*p+1] = 1
        nx[3*p+2] = 1
        rev(nx, p+1)
    
    if prog[15-p] == 4*(x[3*p-3]^1) + 2*x[3*p-2] + x[3*p-1]:
        nx = x.copy()
        nx[3*p] = 1
        nx[3*p+1] = 0
        nx[3*p+2] = 0
        rev(nx, p+1)
    
    if prog[15-p] == 4*(x[3*p-2]^1) + 2*x[3*p-1]:
        nx = x.copy()
        nx[3*p] = 1
        nx[3*p+1] = 0
        nx[3*p+2] = 1
        rev(nx, p+1)
    
    if prog[15-p] == 4*(x[3*p-1]^1) + 1:
        nx = x.copy()
        nx[3*p] = 1
        nx[3*p+1] = 1
        nx[3*p+2] = 0
        rev(nx, p+1)
    
    
    if prog[15-p] == 0:
        nx = x.copy()
        nx[3*p] = 1
        nx[3*p+1] = 1
        nx[3*p+2] = 1
        rev(nx, p+1)
        

        
    


def c(l,regs):
    if l == 7:
        return 0
    if l in [0,1,2,3]:
        return l
    return regs[l-4]

with open("input17.txt") as file:
    t=0
    text = file.read().split("\n\n")
    text[0] = text[0].split("\n")
    regs = []
    for i in range(len(text[0])):
        regs.append(int(text[0][i][12:]))
    l = 0
    i0 = 0
    reg0 = regs.copy()
    prog = list(map(int, text[1][9:].split(",")))
        
    x = {}
    for i in range(-10,0):
        x[i] = 0
    
    rev(x,0)