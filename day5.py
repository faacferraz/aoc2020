def day5p1(inp):
    max_sid = 0
    for s in inp.split('\n'):
        row = s[:7]
        row = row.replace('F', '0')
        row = row.replace('B', '1')
        row = int(row, 2)
        col = s[7:]
        col = col.replace('L', '0')
        col = col.replace('R', '1')
        col = int(col, 2)
        sid = row*8+col
        max_sid = max(sid, max_sid)
    return max_sid

def day5p2(inp):
    sids = set()
    for s in inp.split('\n'):
        row = s[:7]
        row = row.replace('F', '0')
        row = row.replace('B', '1')
        row = int(row, 2)
        col = s[7:]
        col = col.replace('L', '0')
        col = col.replace('R', '1')
        col = int(col, 2)
        sid = row*8+col
        sids.add(sid)

    for i in range(min(sids), max(sids)):
        if i not in sids:
            return i
    return -1

#print(day5p1(inp1))
#print(day5p2(inp1))