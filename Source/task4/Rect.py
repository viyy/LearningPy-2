from Source.lib.List import List
from Source.task4.Line import Line


class Rect:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.lines = List([Line(x1, y1, x2, y2), Line(x2, y2, x3, y3), Line(x3, y3, x4, y4), Line(x4, y4, x1, y1)])

    def where_is_point(self, x, y):
        temp = self.lines.select(lambda l: l.where_point(x, y))
        if temp.all(lambda el: el >= 0) or temp.all(lambda el: el <= 0):
            return 1
        else:
            return 0
