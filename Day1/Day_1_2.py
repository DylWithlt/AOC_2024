
import pandas as pd

def main():
    col_1 = []
    col_2 = []
    with open('./Day1/input.txt','r') as f:
        for line in f:
            n_1, n_2 = line.split("   ")
            col_1.append(int(n_1.strip()))
            col_2.append(n_2.strip())

    print(col_1, col_2)

    df = pd.DataFrame(col_2, columns=["values"])
    print(df)

    value_counts = dict(df["values"].value_counts())
    print(value_counts)

    similarity_score = 0
    for a in col_1:
        needle = str(a)
        similarity_score += a * (value_counts[needle] if needle in value_counts else 0)

    print(similarity_score)


if __name__ == '__main__':
    main()