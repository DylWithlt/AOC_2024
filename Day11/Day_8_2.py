from collections import Counter
from tqdm import tqdm


def get_stone_type(stone):
    if stone == 0:
        return 1
    elif len(str(stone)) % 2 == 0:
        return 2
    else:
        return 3


def simulate_stones(initial_stones, blinks):
    # Use a Counter to track how many stones exist for each unique value
    stone_counts = Counter(initial_stones)

    for _ in range(blinks):
        next_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                next_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                # Split into two stones
                length = len(str(stone))
                half = length // 2
                divider = 10**half
                left = stone // divider
                right = stone % divider
                next_counts[left] += count
                next_counts[right] += count
            else:
                # Multiply by 2024
                next_counts[stone * 2024] += count
        stone_counts = next_counts

    return sum(stone_counts.values())  # Total number of stones


def main():
    with open("./Day11/input.txt", "r") as f:
        initial_stones = list(map(int, f.readline().strip().split(" ")))

    total_stones = simulate_stones(initial_stones, 75)
    print(total_stones)


if __name__ == "__main__":
    main()
