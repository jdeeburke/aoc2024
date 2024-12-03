def main():
    safe = 0
    with open('./input.txt', 'r') as file:

        for line in file:
            levels = list(map(int, line.split(' ')))

            if is_ascending(levels.copy()) or is_descending(levels.copy()):
                safe += 1

    print(safe)

def is_ascending(numbers, used_exception=False):
    for idx, (a, b) in enumerate(zip(numbers, numbers[1:])):
        if a >= b or b > a + 3:
            if used_exception: return False

            list_a = numbers.copy()
            del list_a[idx]

            list_b = numbers.copy()
            del list_b[idx+1]

            return is_ascending(list_a, True) or is_ascending(list_b, True)

    return True

def is_descending(numbers, used_exception=False):
    for idx, (a, b) in enumerate(zip(numbers, numbers[1:])):
        if b >= a or b < a - 3:
            if used_exception: return False

            list_a = numbers.copy()
            del list_a[idx]

            list_b = numbers.copy()
            del list_b[idx+1]

            return is_descending(list_a, True) or is_descending(list_b, True)

    return True

main()