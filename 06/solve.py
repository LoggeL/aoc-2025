def solve1(lines):
    result = 0
    values = []
    for line in lines:
        values.append(line.split())

    for i_row in range(len(values[0])):
        sign = values[-1][i_row]
        count = 0 if sign == "+" else 1
        for i in range(len(values) - 1):
            num = int(values[i][i_row])
            if sign == "*":
                count *= num
            else:
                count += num

        result += count

    return result

def solve2(lines):
    result = 0
    values = []
    for line in lines:
        values.append(list(line))

    sign = None
    stack = []
    for i_col in range(len(values[0])):
        # if sign operator, process previous stack
        if len(values[-1]) > i_col and values[-1][i_col] in "+*":
            if sign is not None:
                print(stack, sign)
                if sign == "+":
                    result += sum(stack)
                else:
                    prod = 1
                    for val in stack:
                        prod *= val
                    result += prod
                stack = []
            sign = values[-1][i_col]

        # build vertical number
        value = ""
        for i_row in range(len(values) - 1):
            char = values[i_row][i_col]
            if char.isdigit():
                value += char

        if value:
            stack.append(int(value))

    # Final stack processing
    if sign == "+":
        result += sum(stack)
    else:
        prod = 1
        for val in stack:
            prod *= val
        result += prod

    return result

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 4277556
    test2_solution = 3263827

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
