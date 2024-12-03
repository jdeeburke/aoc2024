leftList = []
rightDict = {}

with open('./input.txt', 'r') as file:
    for line in file:
        left, right = line.split(' ', 1)
        leftList.append(int(left.strip()))
        right = int(right.strip())

        if right in rightDict:
            rightDict[right] += 1
        else:
            rightDict[right] = 1

similarityScore = 0

for left in leftList:
    if left in rightDict:
        similarityScore += left * rightDict[left]

print(similarityScore)