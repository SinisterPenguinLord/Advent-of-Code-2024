def test(row):
    if row[0] < row[1]:
        row = row[::-1]
    for x in range(len(row)-1):
        if row[x] - row[x+1] not in [1,2,3]:
            return False
    return True

with open("input2.txt") as file:
    t=0
    text = file.read().split("\n")
    for line in text:
        fail = True
        line = line.split(" ")
        row = []
        for elem in line:
            row.append(int(elem))
        for x in range(len(row)):
            cop = row.copy()
            del cop[x]
            print(cop)
            if test(cop):
                fail = False
        if not fail:
            t+= 1
    print(t)