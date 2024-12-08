from pathlib import Path

def find_best_path_in_triangle(input_file: Path) -> int:
    input_text = input_file.read_text()

    input_tree_raw = [[int(num) for num in line.split()] for line in input_text.splitlines()]

    for i in reversed(range(1, len(input_tree_raw))):
        line = input_tree_raw[i]

        for j, (left, right) in enumerate(zip(line, line[1:])):
            input_tree_raw[i-1][j] += max(left, right)

    return input_tree_raw[0][0]

print(find_best_path_in_triangle(Path(__file__).parent / "assets" / "0018_triangle.txt"))
print(find_best_path_in_triangle(Path(__file__).parent / "assets" / "0067_triangle.txt"))
