def day9p1(inp):
    num_list = [int(i) for i in inp.split('\n')]
    num25 = num_list[:25]

    for i in range(25, len(num_list)):
        found = False
        for n in num25:
            tmp = num_list[i] - n
            if tmp in num25 and tmp != n:
                found = True
                num25.pop(0)
                num25.append(num_list[i])
                break

        if not found:
            return num_list[i]



def day9p2(inp, invalid):
    num_list = [int(i) for i in inp.split('\n')]
    elems = []
    last = True

    for n in num_list:
        elems.append(n)
        elems_sum = sum(elems)
        while elems_sum > invalid:
            elems.pop(0)
            elems_sum = sum(elems)

        if elems_sum == invalid:
            return min(elems) + max(elems)


#print(day9p1(inp1))
#print(day9p2(inp1, day9p1(inp1)))