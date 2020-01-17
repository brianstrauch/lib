import unittest

def longest_increasing_subsequence(arr):
  subsequences = []

  for a in arr:
    prefix = []
    for subsequence in subsequences:
      if subsequence[-1] < a and len(subsequence) > len(prefix):
        prefix = subsequence
    subsequences.append(prefix + [a])

  return max(subsequences, key=len)

class TestLIS(unittest.TestCase):
  def test_simple(self):
    self.assertEqual(
      longest_increasing_subsequence([3, 10, 2, 1, 20]),
      [3, 10, 20]
    )

if __name__ == '__main__':
  unittest.main()
