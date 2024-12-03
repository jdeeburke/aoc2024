import re


def main():
    pattern = r'(don\'t\(\)|do\(\))|mul\((\d{1,3}),(\d{1,3})\)'
    sum = 0

    with open('./input.txt', 'r') as file:
        count = True
        for line in file:
            matches = re.findall(pattern, line)
            print(matches)
            for instruction, a, b in matches:
                if instruction == 'don\'t()': count = False
                if instruction == 'do()': count = True
                if count and a != '' and b != '':
                    sum += int(a) * int(b)

    print(sum)


main()