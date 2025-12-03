def solve1(lines):
    total = 0

    for line in lines:
        numbers = list(map(int, list(line)))
        max_index = numbers[:-1].index(max(numbers[:-1]))
        max_index_2 = numbers[max_index + 1 :].index(max(numbers[max_index + 1 :]))

        total += numbers[max_index] * 10 + numbers[max_index + max_index_2 + 1]

    return total


def solve2(lines):
    total = 0
    num_jolts = 12
    for line in lines:
        numbers = list(map(int, list(line)))

        current_jolt_index = 0
        current_jolt = 0
        for i in range(0, num_jolts):
            top_limit = -num_jolts + i + 1 if -num_jolts + i + 1 != 0 else None
            relevant_numbers = numbers[current_jolt_index: top_limit]
            max_jolt_index = relevant_numbers.index(max(relevant_numbers)) + current_jolt_index
            current_jolt += numbers[max_jolt_index] * 10 ** (num_jolts - i - 1)
            current_jolt_index = max_jolt_index + 1

        total += current_jolt
    return total


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 357
    test2_solution = 3121910778619

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
