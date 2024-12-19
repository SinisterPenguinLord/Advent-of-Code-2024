def test(t, i):
    if len(i) == 1:
        return t == i[0]
    j = i[2:]
    return test(t,[i[0]+i[1]]+j) or test(t,[i[0]*i[1]]+j) or test(t,[int(str(i[0])+str(i[1]))]+j)


with open("input7.txt") as file:
    t=0
    text = file.read().split("\n")
    rs = []
    for r in text:
        r = r.split(": ")
        rs.append([int(r[0])] + [list(map(int, r[1].split(" ")))])
    
    for r in rs:
        if test(r[0],r[1]):
            t += r[0]
    print(t)
        
        