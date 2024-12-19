ds = (["S","M"],["M","S"])

with open("input4.txt") as file:
    t=0
    text = file.read().split("\n")
    for x in range(1,len(text)-1):
        for y in range(1,len(text[x])-1):
            if text[x][y] == "A":
                if [text[x+1][y+1],text[x-1][y-1]] in ds and [text[x+1][y-1],text[x-1][y+1]] in ds:
                    t += 1
    print(t)