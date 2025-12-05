def solve1(lines):
    lines = [list(line) for line in lines]
    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@" and count_surroundings(lines, x, y) < 4:
                total += 1
    return total

def count_surroundings(lines, x, y):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(lines) and 0 <= nx < len(lines[ny]) and lines[ny][nx] == "@":
            count += 1
    return count

# Complexity => LOL
def solve2(lines):
    lines = [list(line) for line in lines]
    total = 0
    x = 0
    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if lines[y][x] == "@" and count_surroundings(lines, x, y) < 4:
                total += 1
                lines[y][x] = "."
                x = 0
                y = 0
            x += 1
        y += 1
    return total

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 13
    test2_solution = 43

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
