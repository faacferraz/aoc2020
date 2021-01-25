def day2p1(inp):
    rt = 0
    for i in inp.split('\n'):
        list = i.split()
        ranges = list[0].split('-')
        if int(ranges[0]) <= list[2].count(list[1][0]) <= int(ranges[1]):
            rt+=1
    return rt

def day2p2(inp):
    rt = 0
    for i in inp.split('\n'):
        list = i.split()
        ranges = list[0].split('-')
        if (list[2][int(ranges[0])-1] == list[1][0]) != ((list[2][int(ranges[1])-1] == list[1][0])):
            rt+=1
    return rt

#print(day2p2(inp1))