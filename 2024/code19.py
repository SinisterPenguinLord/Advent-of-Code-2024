def test(deg):
    rs = [deg]
    s = {deg:1}
    while len(rs) > 0:
        r = rs.pop(0)
        #print(r,s[r])
        for tow in tows:
            if r[:len(tow)] == tow:
                if not r[len(tow):] in s:
                    rs.append(r[len(tow):])
                    s[r[len(tow):]] = s[r]
                else:
                    s[r[len(tow):]] += s[r]
        rs = sorted(rs,key=len, reverse=True)
        #print(rs)
#    print()
    try:
        return s[""]
    except:
        return 0


with open("input19.txt") as file:
    t=0
    tows = []
    degs = []
    text = file.read().split("\n\n")
    tows = text[0].split(", ")
    degs = text[1].split("\n")
    
    for deg in degs:
        t += test(deg)
    print(t)