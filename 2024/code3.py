g = ["0","1","2","3","4","5","6","7","8","9",","]

do = True
with open("input3.txt") as file:
    t=0
    text = file.read()
    x = text.find("mul(")
    d = text.find("do()")
    dn = text.find("don't()")
    while x != -1:
        if x == min([x,d,dn]) and do:
            y = text[x:x+13].find(")")
            if y != -1:
                sec = text[x+4:x+y]
                y = sec.find(",")
                lets = True
                for l in sec:
                    if not l in g:
                        lets = False
                if y != -1 and lets:
                    t += int(sec[:y])* int(sec[y+1:])
            
            text = text[x+1:]
        elif d == min([x,d,dn]):
            do = True
            text = text[d+1:]
        elif dn == min([x,d,dn]):
            do = False
            text = text[dn+1:]
        else:
            text = text[x+1:]
        x = text.find("mul(")
        d = text.find("do()")
        dn = text.find("don't()")
        if d == -1:
            d = x+1
        if dn == -1:
            dn = x+1
            
    print(t)