from collections import deque
from tqdm import tqdm


def print_line(files, blanks):
    for i, file in enumerate(files):
        print((str(file[0])) * file[1], end="")
        if len(blanks) > i:
            print("." * blanks[i], end="")

    if len(files) % 2 != 0:
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
            files.append((id_counter, int(c)))
            id_counter += 1
        else:
            blanks.append(int(c))
    if len(puzzle_input) % 2 != 0:
        blanks.append(0)

    print(files, blanks)
    print_line(files, blanks)

    def get_left_most_blank(file_i, file_size):
        """Find the best blank slot for the file."""
        for i in range(file_i):  # Iterate only up to file_i
            if file_size <= blanks[i]:
                return i
        return None

    def mv_file(from_i, to_i):
        """Efficiently move a file from one position to another."""
        # Retrieve the file being moved
        file_id, file_size = files[from_i]
        if from_i > 0:  # Combine the blank before and after the moved file
            blanks[from_i - 1] += blanks[from_i] + file_size
        del blanks[from_i]
        del files[from_i]
        files.insert(to_i + 1, (file_id, file_size))
        blanks[to_i] -= file_size
        blanks.insert(to_i, 0)

    sorted_files = sorted(list(files), key=lambda x: x[0], reverse=True)

    for file_id, file_size in tqdm(sorted_files):
        # Find the current index of the file in the deque
        file_i = next(i for i, f in enumerate(files) if f[0] == file_id)
        blank_id = get_left_most_blank(file_i, file_size)
        # print(file_i, file_id, blank_id)
        if blank_id is not None:
            mv_file(file_i, blank_id)
    print_line(files, blanks)

    checksum = 0
    current_index = 0  # Tracks the current position in the "output" sequence
    for i, (file_id, file_size) in enumerate(files):
        # Add the checksum for the current file
        for offset in range(file_size):
            # print((current_index + offset), file_id, (current_index + offset) * file_id)
            checksum += (current_index + offset) * file_id

        current_index += file_size  # Advance the index by the size of the current file

        # Add the blank space, if it exists
        if i < len(blanks):
            current_index += blanks[i]

    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    main()
