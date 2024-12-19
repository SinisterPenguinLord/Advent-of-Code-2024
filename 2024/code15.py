class box:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def look(self, d):
        if d in [0,2]:
            m1 = gr[self.x-1+d][self.y-1]
            m2 = gr[self.x-1+d][self.y]
            m3 = gr[self.x-1+d][self.y+1]
            if '#' in [m2,m3]:
                return False
            clear = True
            for m in [m1,m2,m3]:
                if type(m) == box:
                    if not m.look(d):
                        clear = False
            return clear
        
        if d == 1:
            m = gr[self.x][self.y+2]
            if m == '.':
                return True
            if m == '#':
                return False
            return m.look(d)
        
        if d == 3:
            m = gr[self.x][self.y-1]
            if m == '#':
                return False
            m = gr[self.x][self.y-2]
            if m in ['.', '#']:
                return True
                
            return m.look(d)
            
    def push(self,d):
        if d in [0,2]:
            m1 = gr[self.x-1+d][self.y-1]
            m2 = gr[self.x-1+d][self.y]
            m3 = gr[self.x-1+d][self.y+1]
            for m in [m1,m2,m3]:
                if type(m) == box:
                    m.push(d)
            gr[self.x][self.y] = '.'
            self.x += d-1
            gr[self.x][self.y] = self
            
        elif d == 1:
            m = gr[self.x][self.y+2]
            if type(m) == box:
                m.push(d)
            gr[self.x][self.y] = '.'
            self.y += 1
            gr[self.x][self.y] = self
            
        elif d == 3:
            m = gr[self.x][self.y-2]
            if type(m) == box:
                m.push(d)
            gr[self.x][self.y] = '.'
            self.y -= 1
            gr[self.x][self.y] = self
        
    def move(self, d):
        (dx,dy) = [(-1,0),(0,1),(1,0),(0,-1)][d]
        m = gr[self.x+dx][self.y+dy]
        if m == ".":
            gr[self.x][self.y] = '.'
            self.x += dx
            self.y += dy
            gr[self.x][self.y] = self
            return True
        if m == "#":
            return False
        if m.move(d):
            gr[self.x][self.y] = '.'
            self.x += dx
            self.y += dy
            gr[self.x][self.y] = self
            return True
        return False
    
    def point(self):
        return self.x*100 + self.y

dirs = ["^",">","v","<"]

def printgr():
    for x in range(len(gr)):
        for y in range(len(gr[0])):
            if (x,y) == (rob.x,rob.y):
                print('@', end = '')
            elif gr[x][y] == '#':
                print('#', end = '')
            elif gr[x][y] == '.' and type(gr[x][y-1]) != box:
                print('.', end = '')
            elif type(gr[x][y]) == box:
                print('[]', end = '')
        print()

with open("input15.txt") as file:
    t=0
    text = file.read().split("\n\n")
    grid = text[0].split("\n")
    gr = [['.' for x in range(2*len(grid[0]))] for y in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "#":
                gr[x][2*y] = "#"
                gr[x][2*y+1] = "#"
            elif grid[x][y] == "O":
                gr[x][2*y] = box(x,2*y)
            elif grid[x][y] == "@":
                rob = box(x,2*y)
    printgr()
    for inp in text[1]:
        if inp != "\n":
#            print(inp)
#            input()
            d = dirs.index(inp)
            (dx,dy) = [(-1,0),(0,1),(1,0),(0,-1)][d]
            (x,y) = (rob.x,rob.y)
            m1 = gr[x+dx][y+dy]
            m2 = gr[x+dx][y+dy-1]
            if m1 != '#':
                if type(m1) == box:
                    if m1.look(d):
                        m1.push(d)
                        rob.x += dx
                        rob.y += dy
                elif type(m2) == box:
                    if m2.look(d):
                        m2.push(d)
                        rob.x += dx
                        rob.y += dy
                else:
                    rob.x += dx
                    rob.y += dy
                    
    printgr()
            #print(gr)
            
    for x in range(len(gr)):
        for y in range(len(gr[0])):
            m = gr[x][y]
            if type(m) == box:
                t += 100*x + y
    print(t)
            
            
        