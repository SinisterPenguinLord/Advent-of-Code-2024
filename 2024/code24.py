def pro(l):
    if l[0] in rs and l[2] in rs:
        if l[1] == "AND" and rs[l[0]] == "1" and rs[l[2]] == "1":
            rs[l[4]] = "1"
            return True
        elif l[1] == "OR" and (rs[l[0]] == "1" or rs[l[2]] == "1"):
            rs[l[4]] = "1"
            return True
        elif l[1] == "XOR" and rs[l[0]] != rs[l[2]]:
            rs[l[4]] = "1"
            return True
        else:
            rs[l[4]] = "0"
            return True
    return False

with open("fixedinput24.txt") as file:
    text = file.read().split("\n\n")
    rs = {}
    for l in text[0].split("\n"):
        l = l.split(": ")
        rs[l[0]] = l[1]

    unp = []
    ins = {}
    rev = {}
    for l in text[1].split("\n"):
        l = l.split(" ")
        ins[(l[0],l[1],l[2])] = l[4]
        ins[(l[2],l[1],l[0])] = l[4]
        rev[l[4]] = (l[0],l[1],l[2])
        if not pro(l):
            unp.append(l)

    while len(unp) > 0:
        l = unp.pop(0)
        if not pro(l):
            unp.append(l)

    b = ["0" for x in range(100)]
    for r in rs:
        if r[0] == "z":
            b[-int(r[1:])-1] = rs[r]


    print(int("".join(b),2))

    a = "x00"
    b = "y00"
    if (a,"XOR",b) in ins and (a,"AND",b) in ins:
        c = ins[(a,"AND",b)]
        if "z00" == ins[(a,"XOR",b)]:
            for x in range(1,45):
                print(x)
                if x < 10:
                    end = "0"+str(x)
                else:
                    end = str(x)
                a = "x"+end
                b = "y"+end
                z = "z"+end
                xor = ins[(a,"XOR",b)]
                if ins[(c,"XOR",xor)] != z:
                    print("problem", z, ins[(c,"XOR",xor)])
                and1 = ins[(a,"AND",b)]
                and2 = ins[(xor,"AND",c)]
                c = ins[and1,"OR",and2]

#z08, thm
#wss, wrm
#z22, hwq
#z29,gbs

gbs,hwq,thm,wrm,wss,z08,z22,z29