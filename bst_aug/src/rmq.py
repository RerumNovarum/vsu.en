import segmenttree

if __name__ == '__main__':
    t = segmenttree.SegmentTree(min, 2**31)
    while True:
        raw = input().split()
        if not raw: break
        cmd, x, y = raw[0], int(raw[1]), int(raw[2])
        if cmd   == 'min':
            print(t.mul(x, y))
        elif cmd == 'put':
            t.put(x, y)
