

def check_update(update, rules):
    for n in range(len(update)):
        if not update[n] in rules:
            continue
        for must_before in rules[update[n]]:
            if must_before in update[:n]:
                return False
    return True



# In order to sort the updates I need to find a way to use the information of the must_after to
# move numbers after the updated numbers and then re-evaluate again from the beginning each time
# step 1. scan for any out of order pages
# step 2. add the out of order page after the number that detected it was out of order (n + 1)
# step 3. repeat until the scan reaches the end without issue

# issue: because the numbers are checked against the previous numbers retroactively we can't add numbers to a running complete update
# we need to basically create a new update each time and check against the newest one.


def sort_update(update, rules):
    while not check_update(update, rules):
        flag = False
        for n in range(len(update)):
            if not update[n] in rules:
                continue

            for must_after in rules[update[n]]:
                if not must_after in update[:n]:
                    continue
                flag = True
                # Create new update with elements must_after must be after
                new_update = []

                # add all things that aren't must_after to the new_update
                found_match = 0
                for x in update[:n+1]:
                    if x == must_after:
                        found_match += 1
                        continue
                    new_update.append(x)

                # add all matches for must_after to new_update
                for x in range(found_match):
                    new_update.append(must_after)

                # add all elements after original n to list.
                new_update.extend(update[n+1:])

                # update the new_update for a new evaluation
                update = new_update
                break
            if flag:
                break
        if flag:
            continue
    return update

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
        if not res:
            update = sort_update(update, rules)
            print("sorted:", update)
            middle = update[int(len(update)/2)]
            middle_totals += middle

    print(middle_totals)

if __name__ == '__main__':
    main()