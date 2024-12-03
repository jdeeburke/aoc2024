def main():
    safe = 0
    with open('./input.txt', 'r') as file:

        for line in file:
            levels = list(map(int, line.split(' ')))
            if is_ascending(levels) or is_descending(levels):
                safe += 1

    print(safe)

def is_ascending(numbers):
    for a, b in zip(numbers, numbers[1:]):
        if a >= b or b > a + 3: return False
    return True

def is_descending(numbers):
    for a, b in zip(numbers, numbers[1:]):
        if b >= a or a > b + 3: return False
    return True

main()