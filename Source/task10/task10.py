import re


def convert_to_postfix(infix: str):
    priors = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
        ")": 1
    }
    inp = re.split(r'(\D)', infix)
    res = []
    stack = []
    for c in inp:
        if c == '':
            continue
        if c not in priors:
            res.append(c)
            continue
        if c == '(':
            stack.append(c)
            continue
        if c == ')':
            t = ''
            while t != '(':
                if len(stack) == 0:
                    raise
                t = stack.pop(-1)
                if t != '(':
                    res.append(t)
            continue
        while len(stack) > 0 and priors[stack[-1]] >= priors[c]:
            res.append(stack.pop(-1))
        stack.append(c)
    while len(stack) > 0:
        res.append(stack.pop(-1))
    return res


def do_math(a, b, action):
    a = float(a)
    b = float(b)
    if action == '^':
        return a**b
    if action == '*':
        return a * b
    if action == '/':
        return b / a
    if action == '+':
        return a + b
    if action == '-':
        return b - a
    raise


def calculate(postfix: list):
    actions = ["^", "*", "/", "+", "-"]
    stack = []
    for c in postfix:
        if c not in actions:
            stack.append(c)
            continue
        if len(stack) < 2:
            raise
        stack.append(do_math(stack.pop(-1), stack.pop(-1), c))
    return stack.pop(-1)


def task10(line: str):
    f = open('output.txt', 'w')
    try:
        res = calculate(convert_to_postfix(line))
        res = int(res) if res.is_integer() else res
    except:
        f.write('Ошибка!')
    else:
        f.write(str(res))
    f.close()


if __name__ == '__main__':
    f = open('input.txt', 'r')
    line = f.readline()
    f.close()
    task10(line)
