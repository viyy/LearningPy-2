from Source.lib.List import List


def task1():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    count = int(lines[0])
    data = List(lines[1].split(' ')).select(lambda x: int(x)).to_array()
    total = 0
    last = 0
    while count > 0:
        i = 0
        maximum = data[i]
        for j in range(len(data)):
            if data[j] >= maximum:
                maximum = data[j]
                i = j
        total += (i+1-last) * maximum
        for k in range(i):
            data[k] = 0
        data[i] = 0
        count -= (i+1-last)
        last = i + 1
    f = open('output.txt', 'w')
    f.write('{}'.format(total))
    f.close()


if __name__ == '__main__':
    task1()
