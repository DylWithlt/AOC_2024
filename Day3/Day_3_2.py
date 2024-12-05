
import re


def main():
    reg2 = r"mul\((\d+),(\d+)\)"
    reg = r"(don\'t\(\))|(do\(\))|(mul\((\d+),(\d+)\))"

    ignoreMul = False
    total = 0

    with open('./Day3/input.txt','r') as f:
        for line in f:
            for match in re.finditer(reg, line):
                if match.group() == "don't()":
                    ignoreMul = True
                elif match.group() == "do()":
                    ignoreMul = False
                else:
                    if not ignoreMul:
                        mul = re.match(reg2, match.group())
                        total += int(mul.group(1)) * int(mul.group(2))

    print(total)



if __name__ == '__main__':
    main()