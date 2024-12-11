from collections import deque


def insert_after(d, value, new_value):
    index = d.index(value)
    d.rotate(-index - 1)  # Rotate to bring the element after 'value' to the front
    d.appendleft(new_value)
    d.rotate(index + 1)  # Rotate back to the original position


def blink(stones):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
            i += 1
        elif len(str(stones[i])) % 2 == 0:
            nums = str(stones[i])
            half = len(nums) // 2
            left = int(nums[:half])
            right = int(nums[half:])
            stones[i] = left
            stones.insert(i + 1, right)
            i += 2
        else:
            stones[i] *= 2024
            i += 1


def main():
    with open("./Day11/input.txt", "r") as f:
        stones = deque(map(int, f.readline().strip().split(" ")))

    print(stones)
    for _ in range(25):
        blink(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
