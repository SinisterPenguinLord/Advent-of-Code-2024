def next(s):
    n = ((s*64)^s) % 16777216
    n = ((n//32)^n) % 16777216
    n = ((n*2048)^n) % 16777216
    return n

with (open("input22.txt") as file):
    text = file.read().split("\n")
    ss = {}
    t = 0
    for n in text:
        n = int(n)
        for _ in range(2000):
            if n in ss:
                n = ss[n]
            else:
                ss[n] = next(n)
                n = ss[n]
    bs = {}
    for (i,n) in enumerate(text):
        cs = set()
        n = int(n)
        for _ in range(1996):
            one = n
            two = ss[one]
            thr = ss[two]
            fou = ss[thr]
            fiv = ss[fou]
            one = one %10
            two = two%10
            thr = thr%10
            fou = fou%10
            fiv = fiv%10
            chas = (two-one,thr-two,thr-fou,fiv-fou)
            if not chas in cs:
                if chas in bs:
                    bs[chas] += fiv
                else:
                    bs[chas] = fiv
                cs.add(chas)
            n = ss[n]
    m = 0
    #print(bs)
    for elem in bs:
        if bs[elem] > m:
                m = bs[elem]
    print(m)
