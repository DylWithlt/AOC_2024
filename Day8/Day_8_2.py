import itertools


def is_in_grid(grid, coord):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b, a[1] * b)


def inv(a):
    return mul(a, -1)


def get_antinodes(grid, pair):
    diff = sub(pair[0], pair[1])

    antinodes = set()

    antinodes.add(pair[0])
    antinodes.add(pair[1])

    count = 1
    while True:
        p0 = add(pair[0], mul(diff, count))
        if not is_in_grid(grid, p0):
            break
        antinodes.add(p0)
        count += 1

    count = 1
    diff = inv(diff)
    while True:
        p1 = add(pair[1], mul(diff, count))
        if not is_in_grid(grid, p1):
            break
        antinodes.add(p1)
        count += 1

    return antinodes


def print_grid(grid):
    for row in grid:
        print("".join(row))


def main():
    with open("./Day8/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]

    # get groups as lists of coordinates
    antenna_groups = {}
    for row_i, row in enumerate(grid):
        for col_i, cell in enumerate(row):
            if cell == ".":
                continue
            if not cell in antenna_groups:
                antenna_groups[cell] = set()
            antenna_groups[cell].add((col_i, row_i))

    antinode_spots = set()
    for s in antenna_groups:
        print(s, antenna_groups[s])
        for pair in itertools.combinations(antenna_groups[s], 2):
            print(pair)
            antinodes = get_antinodes(grid, pair)

            for antinode in antinodes:
                if not is_in_grid(grid, antinode):
                    continue
                antinode_spots.add(antinode)
                if grid[antinode[1]][antinode[0]] == ".":
                    grid[antinode[1]][antinode[0]] = "#"

    print_grid(grid)
    print(len(antinode_spots))


if __name__ == "__main__":
    main()
