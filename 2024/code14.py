import statistics

class rob:
    def __init__(self, x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def up(self):
        self.x = (self.x + self.dx) % 101
        self.y = (self.y + self.dy) % 103
        
        
        

with open("input14.txt") as file:
    t=0
    text = file.read().split("\n")
    tl = 0
    tr = 0
    bl = 0
    br = 0
    robs = []
    for te in text:
        te = te.split(" ")
        (x,y) = tuple(map(int, te[0][2:].split(",")))
        (dx,dy) = tuple(map(int, te[1][2:].split(",")))
        robs.append(rob(x,y,dx,dy))
        
    while True:
        t += 1
        xs = []
        ys = []
        gr = [["." for y in range(101)] for x in range(103)]
        for r in robs:
            r.up()
            (x,y) = (r.x,r.y)
            xs.append(x)
            ys.append(y)
            gr[y][x] = '#'
        if statistics.variance(xs) < 500 and statistics.variance(ys) < 500:
            print(t)
            for r in gr:
                print("".join(r))
    
    for te in text:
        te = te.split(" ")
        (x,y) = tuple(map(int, te[0][2:].split(",")))
        (dx,dy) = tuple(map(int, te[1][2:].split(",")))
        for _ in range(100):
            x = (x + dx) % 101
            y = (y + dy) % 103
        if x < 50 and y < 51:
            tl += 1
        elif x > 50 and y < 51:
            tr += 1
        elif x < 50 and y > 51:
            bl += 1
        elif x > 50 and y > 51:
            br += 1
    print(tl*tr*bl*br)
        
        