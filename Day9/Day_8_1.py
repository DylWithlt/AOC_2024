from collections import deque


def print_line(files, blanks):
    for i, file in enumerate(files):
        print(str(file[0]) * file[1], end="")
        if len(blanks) > i:
            print("." * blanks[i], end="")
    print("." * blanks[-1], end="")
    print("")


def main():
    with open("./Day9/input.txt", "r") as f:
        puzzle_input = f.readline().strip()

    files = deque()  # [(id, amount)]
    blanks = deque()

    id_counter = 0
    for i, c in enumerate(puzzle_input):
        if i % 2 == 0:
            files.append([id_counter, int(c)])
            id_counter += 1
        else:
            blanks.append(int(c))
    if len(puzzle_input) % 2 == 0:
        blanks.append(0)

    print(files, blanks)
    print_line(files, blanks)

    while sum(blanks) != blanks[-1]:
        for i, size in enumerate(blanks):
            if size <= 0:
                continue

            last_file = files[-1]  # Reference the last file without removing it
            last_file_size = last_file[1]

            if last_file_size < size:
                files.insert(i + 1, files.pop())
                blanks[-1] += last_file_size
                blanks[i] -= last_file_size
                blanks.insert(i, 0)
                break
            elif last_file_size == size:
                files.insert(i + 1, files.pop())
                blanks[-1] += last_file_size
                blanks[i] = 0
                blanks.insert(i, 0)
                break
            elif last_file_size > size:
                files[-1][1] -= size  # Modify the size of the last file directly
                files.insert(
                    i + 1, [last_file[0], size]
                )  # Add a new file with the required size
                blanks[-1] += size  # Adjust the trailing blanks
                blanks[i] = 0  # The current blank becomes 0
                blanks.insert(i, 0)  # Insert a placeholder blank
                break

        # print(files, blanks)
        # print_line(files, blanks)
        print(f"{(blanks[-1] / sum(blanks) * 100):.3f}", end="\r")

    print("finished sift...")
    checksum = 0
    counter = 0
    for file in files:
        for i in range(file[1]):
            checksum += file[0] * counter
            counter += 1

    print(checksum)


if __name__ == "__main__":
    main()
