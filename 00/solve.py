def solve1(lines):

    dial = 50
    score = 0

    for line in lines:
        direction, value = line[0], int(line[1:])
        if direction == "L":
            dial = (dial - value) % 100
        elif direction == "R":
            dial = (dial + value) % 100

        # If the dial is at 0, increase score
        if dial == 0:
            score += 1

    return score


def solve2(lines):

    dial = 50
    score = 0

    for line in lines:
        new_dial = None
        direction, value = line[0], int(line[1:])

        if direction == "L":
            new_dial = dial - value
        elif direction == "R":
            new_dial = dial + value

        if new_dial <= 0:
            score += (-new_dial) // 100
            if dial > 0: # if we started above 0, we crossed 0
                score += 1
        elif new_dial >= 100:
            score += new_dial // 100

        dial = new_dial % 100

    # < 5900
    return score

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 3
    test2_solution = 6

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
