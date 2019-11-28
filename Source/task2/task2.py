from Source.lib.List import List


def task2():
    f = open('input.txt', 'r')
    d = f.readline().split(' ')
    f.close()
    k = int(d[0])
    n = int(d[1])
    res = List.repeat(0, n+1)
    res[0] = 1
    for i in range(n):
        for j in range(1, k+1):
            if i+j >= n+1:
                break
            res[i+j] += res[i]
    f = open('output.txt', 'w')
    f.write(str(res.last()))
    f.close()


if __name__ == '__main__':
    task2()