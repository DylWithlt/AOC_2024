import itertools

opts = ["+", "*"]


def can_hit_target(test_val, vals):

    for combo in itertools.product(opts, repeat=len(vals) - 1):
        total = vals[0]
        for i, x in enumerate(vals[1:]):
            if total > test_val:
                break
            op = combo[i]
            if op == "+":
                total += x
            elif op == "*":
                total *= x
        res = total == test_val
        print(test_val, vals, combo, res)
        if res:
            return True
    return False


def main():
    data = []
    with open("./Day7/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            line_split = line.split(":")
            test_val = int(line_split[0])
            vals = [int(x) for x in line_split[1].strip().split(" ")]

            data.append([test_val, vals])

    calib_val = 0
    for dat in data:
        print("---", dat)
        if can_hit_target(dat[0], dat[1]):
            calib_val += dat[0]

    print(calib_val)


if __name__ == "__main__":
    main()
