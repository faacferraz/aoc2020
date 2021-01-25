
def day7p1(inp):
    my_bag = 'shiny gold'
    anti_rule_dict = {}

    for rule in inp.split('\n'):
        tmp = rule.split(' bags contain ')

        if 'no other' in tmp[1]:
            bags = []
        else:
            bags = [b.lstrip().rstrip('.').split(' ', 1)[-1].split(' bag')[0] for b in tmp[1].split(',')]
        for bag in bags:
            if bag not in anti_rule_dict:
                anti_rule_dict[bag] = {tmp[0]}
            else:
                anti_rule_dict[bag].add(tmp[0])

    outsides = set()
    new = {my_bag}
    while new:
        new_new = set()
        for n in new:
            if n in anti_rule_dict:
                for out in anti_rule_dict[n]:
                    if out not in outsides:
                        outsides.add(out)
                        new_new.add(out)
        new = new_new
    return len(outsides)


def day7p2(inp):
    my_bag = 'shiny gold'
    rule_dict = {}

    for rule in inp.split('\n'):
        tmp = rule.split(' bags contain ')
        if 'no other' in tmp[1]:
            bags = []
        else:
            bags = [b.lstrip().rstrip('.').split(' bag')[0].split(' ', 1) for b in tmp[1].split(',')]
        rule_dict[tmp[0]] = bags

    td = {}

    def find_dependencies(bag):
        if bag in td:
            return td[bag]
        total = 0
        if bag not in rule_dict or not rule_dict[bag]:
            return total
        for n, dep in rule_dict[bag]:
            rt = find_dependencies(dep)
            td[dep] = rt
            total += int(n) + int(n)*rt
        return total

    return find_dependencies(my_bag)


#print(day7p1(inp1))
#print(day7p2(inp1))

