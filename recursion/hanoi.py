import random
import unittest

def hanoi(n, src, dst, tmp):
    instructions = []
    if n > 0:
        instructions += hanoi(n - 1, src, tmp, dst)
        instructions += [(n, src, dst)]
        instructions += hanoi(n - 1, tmp, dst, src)
    return instructions

class TestHanoi(unittest.TestCase):
    def test_base(self):
        self.assertEqual(
            hanoi(0, 'A', 'C', 'B'),
            []
        )

    def test_simple(self):
        self.assertEqual(
            hanoi(3, 'A', 'C', 'B'),
            [
                (1, 'A', 'C'),
                (2, 'A', 'B'),
                (1, 'C', 'B'),
                (3, 'A', 'C'),
                (1, 'B', 'A'),
                (2, 'B', 'C'),
                (1, 'A', 'C')
            ]
        )

    def test_random(self):
        for _ in range(100):
            n = random.randint(0, 10)
            self.assertEqual(
                len(hanoi(n, 'A', 'C', 'B')),
                2 ** n - 1
            )

if __name__ == '__main__':
    unittest.main()
