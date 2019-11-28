from Source.lib.List import List


def task3():
    f = open('input.txt', 'r')
    data = f.readline()
    f.close()
    data = data.split(' ')
    s = int(data[0])
    k = int(data[1])
    mx = List.repeat(0, k)
    mn = List.repeat(0, k)
    n = s
    i = 0
    while n > 0:
        if n <= 9:
            mx[i] = n
            n = 0
        else:
            mx[i] = 9
            n -= 9
            i += 1
    n = s - 1
    mn[0] = 1
    i = k - 1
    while n > 0:
        if n <= 9:
            mn[i] = n
            n = 0
        else:
            mn[i] = 9
            n -= 9
            i -= 1
    f = open('output.txt', 'w')
    f.write(mx.aggregate('', lambda seed, x: seed+str(x)) + ' ' + mn.aggregate('', lambda seed, x: seed+str(x)))
    f.close()


if __name__ == '__main__':
    task3()
