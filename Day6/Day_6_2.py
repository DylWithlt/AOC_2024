def get_guard_pos(grid):
    for row_i, row in enumerate(grid):
        for col_i, spot in enumerate(row):
            if spot == "^":
                return (col_i, row_i)


def print_grid(grid):
    for row in grid:
        print("".join([x for x in row]))


def print_grid_with_guard(grid, pos, dir):
    # Create a copy of the grid to modify and display the guard's position and direction
    grid_copy = [row[:] for row in grid]

    # Define guard symbols for each direction
    guard_symbols = {
        (0, -1): "^",  # Up
        (1, 0): ">",  # Right
        (0, 1): "v",  # Down
        (-1, 0): "<",  # Left
    }

    # Mark the guard's position with the appropriate symbol based on its direction
    guard_symbol = guard_symbols.get(dir)
    if guard_symbol:
        grid_copy[pos[1]][pos[0]] = guard_symbol
    # Print the grid with the guard
    for row in grid_copy:
        print("".join([str(x) for x in row]))

    print("")


def rotate_vec_90(dir):
    if dir[1] == -1:
        return (1, 0)
    elif dir[0] == 1:
        return (0, 1)
    elif dir[1] == 1:
        return (-1, 0)
    else:
        return (0, -1)


def move_forward(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def is_within_bounds(pos, grid):
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])


# HMMM
# idea: if each step I check if moving in one direction all the way to the right brings me to an already visited corner then it must form a square
def check_for_loop(grid, start_pos, start_dir):
    visited = set()
    pos = start_pos
    dir = rotate_vec_90(start_dir)

    while True:
        if (pos, dir) in visited:
            return True  # Infinite loop detected
        visited.add((pos, dir))

        next_pos = move_forward(pos, dir)
        if not is_within_bounds(next_pos, grid):  # Guard exits the grid
            return False

        if grid[next_pos[1]][next_pos[0]] == "#":  # Blocker encountered
            dir = rotate_vec_90(dir)
            # print_grid_with_guard(grid, pos, dir)
        else:
            pos = next_pos


def main():
    grid = []
    with open("./Day6/input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    pos = get_guard_pos(grid)
    dir = (0, -1)
    print_grid_with_guard(grid, pos, dir)

    grid[pos[1]][pos[0]] = "."

    init_pos = pos
    # print(pos[0], pos[1])

    pos = init_pos
    dir = (0, -1)

    tested_spots = set()

    loop_counter = 0
    while True:
        search_pos = move_forward(pos, dir)
        if not is_within_bounds(search_pos, grid):
            break

        # print_grid_with_guard(grid, pos, dir)

        cell = grid[search_pos[1]][search_pos[0]]
        if cell != "#":
            if search_pos != init_pos and not (search_pos) in tested_spots:
                bef = grid[search_pos[1]][search_pos[0]]
                grid[search_pos[1]][search_pos[0]] = "#"
                if check_for_loop(grid, pos, dir):
                    loop_counter += 1
                    print(loop_counter)
                grid[search_pos[1]][search_pos[0]] = bef
                tested_spots.add(search_pos)

            pos = search_pos
        else:
            grid[pos[1]][pos[0]] = "C"
            dir = rotate_vec_90(dir)

    print(f"Total:\n{loop_counter}")


if __name__ == "__main__":
    main()
