import math

inp1 = """1000053
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""


def day13p1(inp):
    inp = inp.split('\n')
    earliest = int(inp[0])
    buses = [int(b) for b in inp[1].split(',') if b != 'x']
    #print(earliest)
    #print(buses)
    smallest = float('inf')
    bus_id = None
    for b in buses:
        tmp = b-(earliest%b)
        if tmp == 0:
            return 0
        if tmp < smallest:
            smallest = tmp
            bus_id = b
    #print(smallest, bus_id)
    return smallest*bus_id


def day13p2(inp):
    # Helpful video on Chinese Remainder Theorem: https://www.youtube.com/watch?v=zIFehsBHB8o
    inp = inp.split('\n')
    bus_tuples = [(int(b), (-i%(int(b)))) for i,b in enumerate(inp[1].split(',')) if b != 'x']
    bigNi = []
    bigN = 1

    #print(bus_tuples)
    for n, b in bus_tuples:
        bigN *= n

    for n, b in bus_tuples:
        bigNi.append(int(bigN/n))
        #print(bigNi)

    x = []

    for nb, bn in zip(bus_tuples, bigNi):
        n, b = nb
        tmp = bn % n #xi
        xi = 1
        while (tmp*xi)%n != 1:
            xi+=1
        #print(n, b, bn, xi, int(b*bn*xi))
        x.append(int(b*bn*xi))
    #print(bigN)

    a = int(sum(x))%bigN


    return a





inp2 = """939
67,7,59,61"""

print(day13p1(inp1))

print(day13p2(inp1))