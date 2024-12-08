import itertools


def is_in_grid(grid, coord):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def inv(a):
    return (a[0] * -1, a[1] * -1)


def get_antinodes(pair):
    diff = sub(pair[0], pair[1])

    p0 = add(pair[0], diff)
    p1 = add(pair[1], inv(diff))

    return (p0, p1)


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
            antinodes = get_antinodes(pair)

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
