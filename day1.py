
def day1p1(inp):
    seen = set()
    for i in inp.split():
        n = int(i)
        if (2020 - n) in seen:
            return n*(2020-n)
        seen.add(n)
    return -1

def day1p2(inp):
    seen = set()
    for i in inp.split():
        n = int(i)
        for s in seen:
            tmp = s+n
            if (2020-tmp) in seen:
                return s*n*(2020-tmp)
        seen.add(n)

    return -1



#print(day1p1(inp1))
#print(day1p2(inp1))

