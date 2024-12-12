from collections import deque


def print_grid(grid):
    for row in grid:
        print("".join(row))


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


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def crawl_region(grid, first_pos, visited):
    open_cells = deque([first_pos])
    found_type = grid[first_pos[1]][first_pos[0]]
    visited[first_pos[1]][first_pos[0]] = True

    perimeter = 0
    region = []

    while open_cells:
        cur = open_cells.popleft()
        region.append(cur)

        for dir in directions:
            nxt = add(cur, dir)
            if is_in_grid(grid, nxt):
                nxt_cell = grid[nxt[1]][nxt[0]]
                if not visited[nxt[1]][nxt[0]] and nxt_cell == found_type:
                    visited[nxt[1]][nxt[0]] = True

                    open_cells.append(nxt)
                elif nxt_cell != found_type:
                    perimeter += 1
            else:
                perimeter += 1

    return region, perimeter


def get_region_groups(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    regions = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if not visited[y][x]:
                region, perimeter = crawl_region(grid, (x, y), visited)
                regions.append((region, perimeter))

    return regions


def get_perimeter_from_group(grid, group):
    perimeter = 0
    for cell_pos in group:
        cur = grid[cell_pos[1]][cell_pos[0]]

        for dir in directions:
            nxt = add(cell_pos, dir)

            if nxt in group:
                continue
            if not is_in_grid(grid, nxt) or cur != grid[nxt[1]][nxt[0]]:
                perimeter += 1

    return perimeter


def main():
    with open("./Day12/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]

    print_grid(grid)
    regions = get_region_groups(grid)

    total_price = 0
    for region, perimeter in regions:
        area = len(region)
        cell_type = grid[region[0][1]][region[0][0]]
        price = perimeter * area
        print(f"type {cell_type} perimeter: {perimeter} area: {area} price: {price}")
        total_price += price

    print(total_price)


if __name__ == "__main__":
    main()
