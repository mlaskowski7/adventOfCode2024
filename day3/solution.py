import re

def handle_mul(mul):
    mul = re.sub(r"[^\d,]", "", mul)
    numbers = mul.split(",")

    if len(numbers) != 2:
        raise Exception("Invalid mul catched")

    return int(numbers[0]) * int(numbers[1])

def solve(input_text):
    valid_muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input_text)
    total = 0
    for mul in valid_muls:
        total += handle_mul(mul)
    return total



if __name__ == '__main__':
    all_input = ""
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            all_input += line
    print(solve(all_input))
