def task8():
    f = open('input.txt', 'r')
    line = f.readline()
    f.close()
    op = ['[', '(']
    cl = [']', ')']
    res = 0
    stack = []
    for c in line.strip():
        if c in op:
            stack.insert(0, c)
        else:
            if len(stack) == 0:
                res = -1
                break
            ind = cl.index(c)
            el = stack.pop(0)
            if op.index(el) != ind:
                res += 1
    if len(stack) != 0:
        res = -1
    f = open('output.txt', 'w')
    f.write(str(res))
    f.close()


if __name__ == '__main__':
    task8()
