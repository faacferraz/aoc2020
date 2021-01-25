
def day8p1(inp):
    command_list = inp.split('\n')
    seen = [False] * len(command_list)

    i = 0
    total = 0

    while not seen[i]:
        cmd, val = command_list[i].split()
        seen[i] = True
        if cmd == 'acc':
            total += int(val)
            i += 1
        elif cmd == 'jmp':
            i += int(val)
        else:
            i += 1

    return total

def day8p2(inp):
    command_list = inp.split('\n')
    seen = [False] * len(command_list)

    i = 0
    total = 0

    while not seen[i]:
        cmd, val = command_list[i].split()
        seen[i] = True
        if cmd == 'acc':
            total += int(val)
            i += 1
        elif cmd == 'jmp':
            i += int(val)
        else:
            i += 1

    for j, s in enumerate(seen):
        if s:
            cmd, val = command_list[j].split()
            inv_dic = {'jmp': 'nop', 'nop': 'jmp'}
            if cmd in inv_dic:

                i = 0
                total = 0
                seen2 = [False] * len(command_list)
                while not seen2[i]:
                    cmd, val = command_list[i].split()
                    if i == j:
                        cmd = inv_dic[cmd]

                    seen2[i] = True
                    if cmd == 'acc':
                        total += int(val)
                        i += 1
                    elif cmd == 'jmp':
                        i += int(val)
                    else:
                        i += 1

                    if i >= len(command_list):
                        return total
    return -1

# print(day8p1(inp1))
# print(day8p2(inp1))
