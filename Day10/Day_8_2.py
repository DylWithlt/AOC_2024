from collections import deque


def is_in_grid(grid, coord):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def get_trail_heads(grid):
    trail_heads = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "0":
                trail_heads.add((x, y))

    return trail_heads


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_reachable_nines(grid, trail_head):
    # grid = [row[:] for row in grid]

    reachable_nines = 0

    # closed_nodes = set()
    open_nodes = deque([trail_head])
    while open_nodes:
        cur = open_nodes.pop()
        cur_height = int(grid[cur[1]][cur[0]])
        # closed_nodes.add(cur)

        if cur_height == 9:
            reachable_nines += 1
            continue

        for direction in directions:
            nxt = add(cur, direction)

            if not is_in_grid(grid, nxt):
                continue
            if grid[nxt[1]][nxt[0]] == ".":
                continue
            target_height = int(grid[nxt[1]][nxt[0]])
            if target_height - cur_height == 1:
                open_nodes.append(nxt)
    return reachable_nines


def main():
    with open("./Day10/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]

    trail_heads = get_trail_heads(grid)

    print(trail_heads)
    total = 0
    for trail_head in trail_heads:
        nines = get_reachable_nines(grid, trail_head)
        print(trail_head, nines)
        total += nines

    print(total)


if __name__ == "__main__":
    main()
