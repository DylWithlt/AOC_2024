

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def isDescending(line):
    descending = 0
    ascending = 0

    last = line[0]
    for n in line[1:]:
        if n < last:
            descending += 1
        elif n > last:
            ascending += 1
    return descending > ascending

def comp(last, n, isDecreasing):
     diff = n - last
     return not (diff == 0 or (isDecreasing and diff > 0) or (not isDecreasing and diff < 0) or (abs(diff) > 3))

def isLineValid(line):
    # print(line)
    last = line[0]
    isDecreasing = isDescending(line)


    for n in line[1:]:
        diff = n - last

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

def isValidExcept(line):
    if isLineValid(line):
        return True

    for j in range(len(line)):
        new_list = [x for i, x in enumerate(line) if i != j]

        if isLineValid(new_list):
            return True
        # print("---", new_list, fails)

    return False


def main():
    lines = []
    with open('./Day2/input.txt','r') as f:
        for line in f:
            n_1 = [int(x) for x in line.split(" ")]
            lines.append(n_1)

    valids = 0
    for line in lines:
        res = isValidExcept(line)
        print(line, res)
        if res:
            valids += 1

    print(valids)


if __name__ == '__main__':
    main()