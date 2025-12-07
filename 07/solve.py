import functools

def solve1(lines):
    total = 0 

    start_index = lines[0].index("S")

    tracking_row = [0] * len(lines[0])
    tracking_row[start_index] = 1

    for i_row in range(1, len(lines)):
        new_tracking_row = [0] * len(lines[0])

        # Grab all Splitters in row
        for i_col in range(len(lines[i_row])):
            if lines[i_row][i_col] == "^" and tracking_row[i_col] == 1:
                # Splitter hit
                new_tracking_row[i_col - 1] = 1
                new_tracking_row[i_col + 1] = 1
                total += 1
            elif tracking_row[i_col] == 1:
                new_tracking_row[i_col] = 1
        
        tracking_row = new_tracking_row

    return total

_grid = None
@functools.lru_cache(maxsize=None)
def split_ray(i_row, i_col, direction):
    if direction == "L":
        i_col_split = i_col - 1
    else:
        i_col_split = i_col + 1

    for i_row_split in range(i_row, len(_grid)):
        if i_row_split == len(_grid) - 1:
            # Done
            return 1
        if _grid[i_row_split][i_col_split] == "^":
            return split_ray(i_row_split, i_col_split, "L") + split_ray(i_row_split, i_col_split, "R")

def solve2(lines):
    global _grid
    _grid = tuple(lines)
    split_ray.cache_clear()  # Clear cache for new input
    start_index = lines[0].index("S")

    tracking_row = [0] * len(lines[0])
    tracking_row[start_index] = 1

    for i_row in range(1, len(lines)):
        if lines[i_row][start_index] == "^":
            return split_ray(i_row, start_index, "L") + split_ray(i_row, start_index, "R")

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 21
    test2_solution = 40

    test1_result = solve1(test1)
    test2_result = solve2(test2)

    print("Test 1: " + str(test1_result))
    if test1_solution != test1_result:
        print("Test 1 failed!")
        exit(1)

    print("Solution 1: " + str(solve1(input)))

    print("Test 2: " + str(test2_result))
    if test2_solution != test2_result:
        print("Test 2 failed!")
        exit(1)

    print("Solution 2: " + str(solve2(input)))
