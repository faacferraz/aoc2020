
def day10p1(inp):
    adapters = sorted([int(i) for i in inp.split()])
    adapters.insert(0, 0)
    difs = [0,0,0,1]
    for i in range(1, len(adapters)):
        difs[adapters[i] - adapters[i-1]] += 1
    return difs[3] * difs[1]


def day10p2(inp):
    adapters = sorted([int(i) for i in inp.split()])
    adapters.insert(0, 0)
    ways = [0]*(adapters[-1]+1)
    ways[0] = 1
    for i in range(1, len(adapters)):
        ways[adapters[i]] = ways[adapters[i]-1] + ways[adapters[i]-2] + ways[adapters[i]-3]
    return ways[-1]

#print(day10p1(inp1))
#print(day10p2(inp1))