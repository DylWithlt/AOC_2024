

def main():
    col_1 = []
    col_2 = []
    with open('./Day1/input.txt','r') as f:
        for line in f:
            n_1, n_2 = line.split("   ")
            col_1.append(int(n_1.strip()))
            col_2.append(int(n_2.strip()))

    print(col_1, col_2)

    col_1.sort()
    col_2.sort()

    print(col_1, col_2)

    total = 0
    for a, b in zip(col_1, col_2):
        total += abs(a - b)

    print(total)


if __name__ == '__main__':
    main()