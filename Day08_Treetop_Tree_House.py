from collections import defaultdict

InputList = []
with open("test.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

Height = len(InputList)
Width = len(InputList[0])
TreeGridDict = defaultdict()

for y, u in enumerate(InputList):
    for x, n in enumerate(u):
        TreeGridDict[(x,y)] = int(n)

HighestTreeEver = max(TreeGridDict.values())

VisibleSet = set()

#Going Down
for x in range(Width):
    Threshold = -1
    for y in range(Height):
        if TreeGridDict[(x,y)] > Threshold:
            VisibleSet.add((x,y))
            Threshold = TreeGridDict[(x,y)]
            if Threshold == HighestTreeEver:
                break

#Going up
for x in range(Width):
    Threshold = -1
    for y in reversed(range(Height)):
        if TreeGridDict[(x,y)] > Threshold:
            VisibleSet.add((x,y))
            Threshold = TreeGridDict[(x,y)]
            if Threshold == HighestTreeEver:
                break
#Going right
for y in range(Height):
    Threshold = -1
    for x in range(Width):
        if TreeGridDict[(x,y)] > Threshold:
            VisibleSet.add((x,y))
            Threshold = TreeGridDict[(x,y)]
            if Threshold == HighestTreeEver:
                break

#Going left
for y in range(Height):
    Threshold = -1
    for x in reversed(range(Width)):
        if TreeGridDict[(x,y)] > Threshold:
            VisibleSet.add((x,y))
            Threshold = TreeGridDict[(x,y)]
            if Threshold == HighestTreeEver:
                break

Part1Answer = len(VisibleSet)

Directions = [(0,1),(0,-1),(1,0),(-1,0)]
HighestScore = 0
for x in range(1, Width-1):
    for y in range(1, Height-1):
        OriginalHeight = TreeGridDict[(x,y)]
        ScoreList = []
        for dx, dy in Directions:
            DirectionScore = 0
            GX,GY = x,y
            while True:
                GX,GY = GX+dx, GY+dy
                if GX < 0 or GY < 0 or GX >= Width or GY >= Height:
                    break
                DirectionScore += 1
                if TreeGridDict[(GX,GY)] >= OriginalHeight:
                    break
            ScoreList.append(DirectionScore)
        A,B,C,D = ScoreList
        NewScore = A*B*C*D
        if NewScore > HighestScore:
            HighestScore = NewScore
            ScenicTree = (x,y)

Part2Answer = HighestScore

print(ScenicTree)
print(f"{Part1Answer = }")
print(f"{Part2Answer = }")