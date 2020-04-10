import unittest

class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.size = 0
        self.root = Node()

    def insert(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

        self.size += 1

    def find(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end

class TestTreap(unittest.TestCase):
    def test_insert(self):
        t = Trie()
        self.assertEqual(t.size, 0)
        t.insert('test')
        self.assertEqual(t.size, 1)

    def test_find(self):
        t = Trie()
        t.insert('test')
        self.assertTrue(t.find('test'))
        self.assertFalse(t.find('other'))

    def test_prefix(self):
        t = Trie()
        t.insert('prefixtest')
        self.assertFalse(t.find('prefix'))
        t.insert('prefix')
        self.assertTrue(t.find('prefix'))

if __name__ == '__main__':
    unittest.main()
