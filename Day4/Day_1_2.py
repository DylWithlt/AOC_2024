
import numpy as np

diag =  np.array([
        ["M", None, "S"],
        [None, "A", None],
        ["M", None, "S"],
    ])

patterns = [
    diag,
    np.rot90(diag),
    np.rot90(np.rot90(diag)),
    np.rot90(np.rot90(np.rot90(diag)))
]

wildcard = "*"

def match_pattern(grid, pattern):
    matches = 0
    mask = pattern != wildcard

    print(mask)
    for i in range(grid.shape[0] - pattern.shape[0] + 1):
        for j in range(grid.shape[1] - pattern.shape[1] + 1):
            sub_grid = grid[i:i+pattern.shape[0], j:j+pattern.shape[1]]
            if np.array_equal(sub_grid[mask], pattern[mask]):
                matches += 1
    return matches

def main():
    # for pattern in patterns:
    #     for row in pattern:
    #         print(" ".join(str(x) for x in row))
    print(patterns)

    grid = []
    with open('./Day4/input.txt','r') as f:
        for line in f:
            grid.append(list(line.strip()))
    grid = np.array(grid)
    print(grid)


    total = 0
    for pattern in patterns:
        pattern = np.where(pattern == None, wildcard, pattern)
        matches = match_pattern(grid, pattern)
        print(f"Matches for pattern:\n{pattern}\n{matches}")
        total += matches

    print(total)



if __name__ == '__main__':
    main()