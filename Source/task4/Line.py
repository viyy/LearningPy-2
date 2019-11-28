class Line:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def where_point(self, x, y):
        t = self
        s = (t.x2 - t.x1) * (y - t.y1) - (t.y2 - t.y1) * (x - t.x1)
        if s > 0:
            return 1
        elif s < 0:
            return -1
        else:
            return 0
