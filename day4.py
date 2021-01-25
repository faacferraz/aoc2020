
def day4p1(inp):
    rt = 0
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in inp.split('\n\n'):
        valid = True
        for k in keys:
            if not passport.count(k):
                valid = False
                break
        if valid:
            rt += 1
    return rt


def day4p2(inp):
    rt = 0
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in inp.split('\n\n'):
        passport_keys = {kv.split(':')[0]: kv.split(':')[1] for kv in passport.split()}
        print(passport_keys)
        ecl_options = 'amb blu brn gry grn hzl oth'.split()
        valid = True
        for k in keys:
            if not valid:
                break

            if k not in passport_keys:
                valid = False
            else:
                val = passport_keys[k]
                if k == 'byr':
                    if not (len(val) == 4 and (1920 <= int(val) <= 2002)):
                        valid = False
                elif k == 'iyr':
                    if not (len(val) == 4 and (2010 <= int(val) <= 2020)):
                        valid = False
                elif k == 'eyr':
                    if not (len(val) == 4 and (2020 <= int(val) <= 2030)):
                        valid = False
                elif k == 'hgt':
                    if 'cm' in val:
                        tmp = val.split('cm')[0]
                        if not (150 <= int(tmp) <= 193):
                            valid = False
                    elif 'in' in val:
                        tmp = val.split('in')[0]
                        if not (59 <= int(tmp) <= 76):
                            valid = False
                    else:
                        print(passport_keys)
                        valid = False
                elif k == 'hcl':
                    if val[0] != '#' or len(val) != 7:
                        valid = False
                    for char in range(1, len(val)):
                        if val[char] not in "01234566789abcdef":
                            valid = False
                            break
                elif k == 'ecl':
                    if val not in ecl_options:
                        valid = False
                elif k == 'pid':
                    if not (len(val) == 9 and val.isdigit()):
                        valid = False
        if valid:
            rt += 1
    return rt

# print(day4p1(inp1))
# print(day4p2(inp1))
