

def check_update(update, rules):
    for n in range(len(update)):
        if not update[n] in rules:
            continue
        for must_before in rules[update[n]]:
            if must_before in update[:n]:
                return False
    return True

def main():
    read_rules = []
    updates = []

    switchInputDestination = False
    with open('./Day5/input.txt','r') as f:
        for line in f:
            if line == "\n":
                switchInputDestination = True
                continue

            if switchInputDestination:
                updates.append(list(map(int, line.strip().split(","))))
            else:
                read_rules.append(list(map(int, line.strip().split("|"))))

    print(updates)

    rules = {}
    for rule in read_rules:
        if not rule[0] in rules:
            rules[rule[0]] = []
        rules[rule[0]].append(rule[1])

    print(rules)

    middle_totals = 0
    for update in updates:
        res = check_update(update, rules)

        print(res, update)
        if res:
            middle = update[int(len(update)/2)]
            print(middle)
            middle_totals += middle

    print(middle_totals)

if __name__ == '__main__':
    main()