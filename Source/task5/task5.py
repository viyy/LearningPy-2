m = []
count = 0


def available(x, y, m):
    for i in range(len(m)):
        # point
        if m[i][0] == x or m[i][1] == y:
            return False
        # diag1
        if m[i][1] - m[i][0] == y - x:
            return False
        # diag2
        if m[i][1] + m[i][0] == y + x:
            return False
        # knights
        if m[i][0] + 1 == x and m[i][1] - 2 == y:
            return False
        if m[i][0] + 1 == x and m[i][1] + 2 == y:
            return False
        if m[i][0] + 2 == x and m[i][1] - 1 == y:
            return False
        if m[i][0] + 2 == x and m[i][1] + 1 == y:
            return False
    return True


def do_task(sx, n, k):
    global count, m
    if len(m) == k:
        count += 1
        return
    for x in range(sx, n):
        for y in range(0, n):
            if available(x, y, m):
                m.append((x, y))
                do_task(x+1, n, k)
                m.pop(-1)


def task5():
    global m, count
    f = open('input.txt', 'r')
    n, k = map(int, f.readline().split(" "))
    f.close()
    count = 0
    m = []
    do_task(0, n, k)
    f = open('output.txt', 'w')
    f.write(str(count))
    f.close()


if __name__ == '__main__':
    task5()
