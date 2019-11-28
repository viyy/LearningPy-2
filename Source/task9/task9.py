_n: int
_m: int
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_len = len(Alpha)
_deltas = [[-1, -1], [-1, 0], [-1, 1],
           [0, -1],           [0, 1],
           [1, -1],  [1, 0],  [1, 1]]


def find_path(grid, i, j, nxt):
    if nxt == alp_len:
        return 1
    res = 0
    t = 0
    for delta in _deltas:
        x = i + delta[0]
        y = j + delta[1]
        if x < 0 or x >= _n or y < 0 or y >= _m:
            continue
        if grid[x][y] != Alpha[nxt]:
            continue
        t = find_path(grid, x, y, nxt + 1)
        if t > res:
            res = t
    return 1 + res


def task9(grid):
    global _n, _m
    _n = len(grid)
    _m = len(grid[0])
    res = 0
    for i in range(_n):
        for j in range(_m):
            if grid[i][j] != Alpha[0]:
                continue
            t = find_path(grid, i, j, 1)
            if t > res:
                res = t
    return res
