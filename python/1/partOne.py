# Get input lists
leftList = []
rightList = []

with open('./input.txt', 'r') as file:
    for line in file:
        left, right = line.split(' ', 1)
        leftList.append(int(left.strip()))
        rightList.append(int(right.strip()))

# Sort each list
leftSorted = sorted(leftList)
rightSorted = sorted(rightList)

print(leftSorted)
print(rightSorted)

# Get absval difference for each number in the list
# Add up all the differences
differenceSum = 0
idx = 0
while idx < len(leftSorted):
    differenceSum += abs(leftSorted[idx] - rightSorted[idx])
    idx += 1

print(differenceSum)