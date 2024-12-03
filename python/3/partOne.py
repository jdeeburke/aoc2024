import re


def main():
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    sum = 0

    with open('./input.txt', 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)

            for a, b in matches:
                sum += int(a) * int(b)

    print(sum)
main()