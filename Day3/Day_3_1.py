
import re


def main():
    reg = r"mul\((\d+),(\d+)\)"
    foundMuls = []

    with open('./Day3/input.txt','r') as f:
        for line in f:
            foundMuls.extend(re.findall(reg, line))

    total = 0
    for g in foundMuls:
        total += int(g[0]) * int(g[1])

    print(total)


if __name__ == '__main__':
    main()