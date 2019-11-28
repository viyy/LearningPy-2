from Source.task4.Rect import Rect


def task4():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    count = 0
    for i in range(1, n+1):
        px, py, x1, y1, x2, y2, x3, y3, x4, y4 = [int(s) for s in lines[i].split(' ')]
        count += Rect(x1, y1, x2, y2, x3, y3, x4, y4).where_is_point(px, py)
    f = open('output.txt', 'w')
    f.write(str(count))
    f.close()


if __name__ == '__main__':
    task4()
