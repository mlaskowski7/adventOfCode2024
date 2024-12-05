def get_middle(line: str) -> int:
    parts = line.split(',')
    return int(parts[int((len(parts) - 1) / 2)])


def check_rule(rule: str, update: str) -> bool:
    parts = rule.split('|')
    before, after = int(parts[0]), int(parts[1])
    update = list(map(int, update.split(',')))

    for i in range(1, len(update)):
        if update[i] == before and update[i - 1] == after:
            return False
    return True


def main():
    rules = []
    updates = []

    with open('input.txt', 'r') as input_file:
        first_section = True
        for line in input_file:
            if line == '\n':
                first_section = False
                continue
            if first_section:
                rules.append(line.strip())
            else:
                updates.append(line.strip())

    total = 0
    for update in updates:
        is_ok = True
        for rule in rules:
            if not check_rule(rule, update):
                is_ok = False
                break
        if is_ok:
            total += get_middle(update)

    print(total)


if __name__ == '__main__':
    main()
