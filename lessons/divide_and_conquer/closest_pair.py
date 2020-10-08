import math
import sys


def closest(points):
    Px = [*points]
    Px.sort(key=lambda point: point.x)
    Py = [*points]
    Py.sort(key=lambda point: point.y)

    return closest_pair(Px, Py)


# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/closepoints.pdf
def closest_pair(Px, Py):
    if len(Px) <= 2:
        return bruteForce(Px)

    pivot = len(Px)//2
    mid = Px[pivot]
    dl = closest_pair(Px[:pivot], Py)
    dr = closest_pair(Px[pivot:], Py)

    d = min(dl, dr)
    # Merge only some points and order by .y
    Sy = []
    for p in Py:
        _d = abs(p.x - mid.x)
        if _d < d:
            Sy.append(p)

    for i in range(len(Sy)):
        j = i + 1
        while j < min(7, len(Sy)):
            if (Sy[j].y - Sy[i].y) < d:
                d = dist(Sy[i], Sy[j])
            j += 1

    return d


def bruteForce(P):
    min_val = float('inf')
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val


def dist(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return math.sqrt(x**2 + y**2)


tests = [
    [
        [2, 3], [12, 20], [40, 50], [5, 1], [12, 10], [3, 4], [2, 7],
        [4, 3], [1, 9], [4, 5], [1, 1], [9, 12], [30, 4], [22, 7],
        [11, 3]
    ]
]


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


for items in tests:
    points = []
    for [x, y] in items:
        points.append(Point(x, y))
    actual = round(closest(points), 6)
    expected = round(bruteForce(points), 6)
    if actual != expected:
        print(f"\033[91m {actual} # {expected}")
    else:
        print(f"\033[92m {expected} -> OK")
