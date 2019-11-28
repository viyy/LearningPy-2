from typing import List


def create_input_txt(lines):
    f = open('input.txt', 'w')
    f.write("\n".join(lines).strip())
    f.close()


def read_output():
    try:
        f = open('output.txt', 'r')
        res = int(f.read())
        f.close()
    except:
        return None
    else:
        return res


def read_output_raw():
    try:
        f = open('output.txt', 'r')
        res = f.read()
        f.close()
    except:
        return None
    else:
        return res


def read_grid_int():
    grid: List[List[int]] = []
    f = open('output.txt', 'r')
    try:
        lines = f.readlines()
        for line in lines:
            grid.append(list(map(int, line.split(' '))))
        f.close()
    except:
        return None
    finally:
        f.close()
    return grid
