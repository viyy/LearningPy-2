def task6():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    op = ['{', '[', '(']
    cl = ['}', ']', ')']
    res = []
    for line in lines:
        stack = []
        correct = True
        for c in line.strip():
            if c in op:
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    correct = False
                    break
                ind = cl.index(c)
                el = stack.pop(0)
                if op.index(el) != ind:
                    correct = False
                    break
        if len(stack) != 0:
            correct = False
        res.append(0 if correct else 1)
    f = open('output.txt', 'w')
    f.write("".join([str(s) for s in res]))
    f.close()


if __name__ == '__main__':
    task6()
