import random
import unittest

def mergesort(arr):
    if len(arr) < 2:
        return arr

    m = len(arr) // 2
    a = mergesort(arr[:m])
    b = mergesort(arr[m:])
    return merge(a, b)

def merge(a, b):
    arr = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1
    arr += a[i:]
    arr += b[j:]
    return arr

class TestMergesort(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(
            merge(['A', 'C'], ['B', 'D']),
            ['A', 'B', 'C', 'D']
        )

    def test_base(self):
        self.assertEqual(mergesort([]), [])

    def test_simple(self):
        self.assertEqual(
            mergesort(['C', 'A', 'D', 'B']),
            ['A', 'B', 'C', 'D']
        )

    def test_random(self):
        for _ in range(100):
            n = random.randint(0, 10)
            arr = [random.randint(0, 10) for _ in range(n)]
            self.assertEqual(mergesort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()
