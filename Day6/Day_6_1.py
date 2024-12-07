

def get_guard_pos(grid):
    for row_i, row  in enumerate(grid):
        for col_i, spot in enumerate(row):
            print(col_i, row_i, spot)
            if spot == "^":
                return (col_i, row_i)

def rotate_vec_90(dir):
    if dir[1] == -1:
        return (1, 0)
    elif dir[0] == 1:
        return (0, 1)
    elif dir[1] == 1:
        return (-1, 0)
    else:
        return (0, -1)

def print_grid(grid):
    for row in grid:
        print("".join(row))

def main():
    grid = []
    with open('./Day6/input.txt','r') as f:
        for line in f:
           grid.append(list(line.strip()))

    print(grid)

    pos = get_guard_pos(grid)
    print(pos[0], pos[1])

    steps = 1
    dir = (0, -1)
    while True:
        search_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if search_pos[1] < 0 or search_pos[1] >= len(grid):
            break
        if search_pos[0] < 0 or search_pos[0] >= len(grid[search_pos[1]]):
            break

        if grid[search_pos[1]][search_pos[0]] != "#":
            if grid[search_pos[1]][search_pos[0]] != "X":
                steps += 1
            grid[pos[1]][pos[0]] = "X"
            grid[search_pos[1]][search_pos[0]] = "^"
            pos = search_pos
            # print_grid(grid)
        else:
            dir = rotate_vec_90(dir)

    print(steps)

if __name__ == '__main__':
    main()