def check_if_level_is_safe(report):
    sorted_inc = sorted(report)
    sorted_desc = sorted(report, reverse=True)
    if sorted_inc != report and sorted_desc != report:
        return False

    for j in range(0, len(report) - 1):
        if abs(report[j + 1] - report[j]) < 1 or abs(report[j + 1] - report[j]) > 3:
            return False

    return True

levels = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        reports = list(map(int, line.strip().split(" ")))
        levels.append(reports)


safe_levels = 0

for level in levels:
    if check_if_level_is_safe(level):
        safe_levels += 1
        continue

    safe = False
    for i in range(len(level)):
        temp_report = level[:i] + level[i + 1:]
        if check_if_level_is_safe(temp_report):
            safe = True
            break

    if safe:
        safe_levels += 1

print(f"safe levels are = {safe_levels}")
