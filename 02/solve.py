def solve1(lines):
    # only one line
    lines = lines[0].split(",")
    score = 0
    for line in lines:
        start, end = line.split("-")
        for num in range(int(start), int(end) + 1):
            if check_double_sequence(num):
                # print(f"Found double id: {num}")
                score += num
    return score

def check_double_sequence(num):
    if len(str(num)) % 2 == 1:
        return False
    num_str = str(num)
    front_str = num_str[: len(num_str) // 2]
    back_str = num_str[len(num_str) // 2 :]
    return front_str == back_str

def check_multi_sequence(num):
    for seq_len in range(1, len(str(num)) // 2 + 1):
        num_str = str(num)
        num_check = num_str[:seq_len]
        for i in range(seq_len, len(num_str), seq_len):
            if num_str[i : i + seq_len] != num_check:
                break
        else:
            return True

def solve2(lines):
    # only one line
    lines = lines[0].split(",")
    score = 0
    for line in lines:
        start, end = line.split("-")
        for num in range(int(start), int(end) + 1):
            if check_multi_sequence(num):
                print(f"Found multi id: {num}")
                score += num
    return score

if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 1227775554
    test2_solution = 4174379265

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
