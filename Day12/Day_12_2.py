from collections import deque, defaultdict


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


directions = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
]  # up left down right (counter-clockwise)


def get_edge_index(dir):
    return 0 if dir == directions[1] or dir == directions[3] else 1  # left or right


def get_edge_direction(pos1, dir):
    idx = get_edge_index(dir)
    return (pos1[idx], dir)  # Group by y-axis, direction is left or right


def get_edge(pos1, pos2):
    # Get the edge between pos1 and pos2, order the edge to avoid duplication
    return tuple(sorted([pos1, pos2]))


def crawl_region(grid, first_pos, visited):
    open_cells = deque([first_pos])
    found_type = grid[first_pos[1]][first_pos[0]]
    visited[first_pos[1]][first_pos[0]] = True

    perimeter_edges = defaultdict(list)  # To store edges grouped by direction and axis
    region = []

    while open_cells:
        cur = open_cells.popleft()
        region.append(cur)

        for dir in directions:
            nxt = add(cur, dir)
            if is_in_grid(grid, nxt):
                nxt_cell = grid[nxt[1]][nxt[0]]

                if nxt_cell == found_type:
                    # If the adjacent cell is part of the same region, continue traversal
                    if not visited[nxt[1]][nxt[0]]:
                        visited[nxt[1]][nxt[0]] = True
                        open_cells.append(nxt)
                else:
                    # If the adjacent cell is of a different region, record the edge
                    edge_dir = get_edge_direction(cur, dir)
                    perimeter_edges[edge_dir].append(cur)
            else:
                # Out of bounds: this is an external edge
                edge_dir = get_edge_direction(cur, dir)
                perimeter_edges[edge_dir].append(cur)

    print(perimeter_edges)
    # Now, merge adjacent edges for each group
    unique_edges = 0
    for key in perimeter_edges:
        edges = perimeter_edges[key]
        # Sort the edges by the relevant axis (x or y)
        idx = 1 if get_edge_index(key[1]) == 0 else 0
        edges = sorted(edges, key=lambda x: x[idx])

        print(edges)

        # Count contiguous groups of edges
        group_count = 1  # At least one group exists
        for i in range(1, len(edges)):
            # If the current edge is not adjacent to the previous one, increment the group count
            if (
                edges[i][idx] != edges[i - 1][idx] + 1
            ):  # Checking adjacency based on x or y
                group_count += 1

        unique_edges += group_count

    return region, unique_edges


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
