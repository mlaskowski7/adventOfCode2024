left_list = []
right_list = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        parts = line.split("   ")
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

left_list.sort()
right_list.sort()

if len(left_list) != len(right_list):
    raise Exception("Incorrect input, lengths are different")

total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)