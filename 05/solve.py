def solve1(lines):
    total = 0

    # split in ranges and ids (split by blank line)
    separator_index = lines.index("")
    ranges = lines[:separator_index]
    for i in range(len(ranges)):
        ranges[i] = list(map(int, ranges[i].split("-")))
    ids = lines[separator_index + 1:]

    for id in ids:
        id_num = int(id)
        for r in ranges:
            if r[0] <= id_num <= r[1]:
                total += 1
                break

    return total


def solve2(lines):
    total = 0

    # split in ranges and ids (split by blank line)
    separator_index = lines.index("")
    ranges = lines[:separator_index]
    for i in range(len(ranges)):
        ranges[i] = list(map(int, ranges[i].split("-")))

    ranges.sort(key=lambda x: x[0])

    # merge
    merged = []
    for start,end in ranges:
        if merged and start < merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    # count merged
    for i in range(len(merged)):
        total += merged[i][1] - merged[i][0] + 1

    return total

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 3
    test2_solution = 14

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
