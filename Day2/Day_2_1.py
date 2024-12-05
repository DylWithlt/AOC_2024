

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def isLineValid(line):
    # print(line)
    last = line[0]
    isDecreasing = line[0] > line[1]
    for n in line[1:]:
        diff = n - last

        # print(diff)
        if diff == 0:
            return False

        if isDecreasing and diff > 0:
            return False
        elif not isDecreasing and diff < 0:
            return False

        if abs(diff) > 3:
            return False
        last = n
    return True

def main():
    lines = []
    with open('./Day2/input.txt','r') as f:
        for line in f:
            n_1 = [int(x) for x in line.split(" ")]
            lines.append(n_1)

    valids = 0
    for line in lines:
        res = isLineValid(line)
        if res:
            valids += 1

    print(valids)


if __name__ == '__main__':
    main()