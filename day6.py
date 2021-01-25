def day6p1(inp):
    count = 0
    for group in inp.split('\n\n'):
        s = set(group)
        if '\n' in s:
            s.remove('\n')
        count += len(s)
    return count

def day6p2(inp):
    count = 0
    for group in inp.split('\n\n'):
        sets = [set(s) for s in group.split()]
        matching = sets[0]
        for i in range(1, len(sets)):
            matching = matching & sets[i]
        count += len(matching)
    return count


#print(day6p1(inp1))
#print(day6p2(inp1))