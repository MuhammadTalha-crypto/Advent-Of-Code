def input_reader(f: str) -> str:
    with open(f, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[0]


DATA = input_reader("test.txt")


def first_marker(data_stream: str, buffer_size: int = 4) -> int:
    begin_idx = ending_idx = 0
    buffer = set()
    while len(buffer) < buffer_size:
        buffer.add(data_stream[ending_idx])
        ending_idx += 1
        if len(buffer) < (ending_idx - begin_idx):
            begin_idx += 1
            ending_idx = begin_idx
            buffer.clear()
    return ending_idx


def main():
    print(first_marker(DATA, 4))  # First Answer: 1275
    print(first_marker(DATA, 14))  # Second Answer: 3605


if __name__ == "__main__":
    main()