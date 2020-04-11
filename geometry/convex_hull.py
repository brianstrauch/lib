import unittest

def is_counterclockwise(a, b, c):
    return (b[1] - a[1]) * (c[0] - b[0]) < (c[1] - b[1]) * (b[0] - a[0])

def convex_hull(points):
    hull = []
    curr = min(points)

    while True:
        hull.append(curr)

        best = points[0]
        for p in points:
            if curr == best or is_counterclockwise(curr, best, p):
                best = p
        curr = best
        if curr == hull[0]:
            break

    return hull

class TestConvexHull(unittest.TestCase):
    def test_triangle(self):
        triangle = [(0, 0), (0, 1), (1, 0)]
        self.assertEqual(convex_hull(triangle), triangle)

    def test_triangle_with_inside_point(self):
        triangle = [(0, 0), (0, 1), (1, 0), (0.25, 0.25)]
        self.assertEqual(convex_hull(triangle), triangle[:3])

if __name__ == '__main__':
    unittest.main()
