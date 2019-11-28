class Rect:
    def __init__(self, n, max_x, max_y):
        self.x1 = max_x + 1
        self.y1 = max_y + 1
        self.x2 = -1
        self.y2 = -1
        self.points = []
        self.n = n

    def add_point(self, x, y):
        self.points.append((x, y))

    def calculate_bounds(self):
        for p in self.points:
            if p[0] < self.x1:
                self.x1 = p[0]
            if p[0] > self.x2:
                self.x2 = p[0]
            if p[1] < self.y1:
                self.y1 = p[1]
            if p[1] > self.y2:
                self.y2 = p[1]
        self.x2 += 1
        self.y2 += 1

    def to_string(self):
        return '{} {} {} {}'.format(self.x1, self.y1, self.x2, self.y2)


def task7():
    f = open('input.txt', 'r')
    n, m, k = map(int, f.readline().split(' '))
    grid = []
    for i in range(n):
        line = f.readline().split(' ')
        grid.append(list(map(int, line)))
    f.close()
    grid.reverse()
    rects = []
    for i in range(k):
        rects.append(Rect(i+1, m, n))
    for y in range(n):
        for x in range(m):
            if grid[y][x] != 0:
                rects[grid[y][x]-1].add_point(x, y)
    f = open('output.txt', 'w')
    o = ''
    for i in range(k):
        rects[i].calculate_bounds()
        o += rects[i].to_string() + '\n'
    o.rstrip()
    f.write(o)
    f.close()


if __name__ == '__main__':
    task7()
