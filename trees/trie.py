import unittest

class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        curr.count += 1

        for c in s:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
            curr.count += 1
        curr.is_end = True

    def size(self):
        return self.root.count

    def find(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr

    def contains(self, s):
        node = self.find(s)
        return node and node.is_end

    def count(self, s):
        node = self.find(s)
        return node.count if node else 0

class TestTreap(unittest.TestCase):
    def test_size(self):
        t = Trie()
        self.assertEqual(t.size(), 0)

    def test_insert(self):
        t = Trie()
        self.assertEqual(t.size(), 0)
        t.insert('test')
        self.assertEqual(t.size(), 1)

    def test_find(self):
        t = Trie()
        t.insert('test')
        n = t.find('test')
        self.assertIsNotNone(n)

    def test_contains(self):
        t = Trie()
        t.insert('test')
        self.assertTrue(t.contains('test'))
        self.assertFalse(t.contains('nonexistent'))

    def test_prefix(self):
        t = Trie()
        t.insert('prefixtest')
        self.assertFalse(t.contains('prefix'))
        t.insert('prefix')
        self.assertTrue(t.contains('prefix'))

    def test_count(self):
        t = Trie()
        t.insert('aa')
        t.insert('ab')
        self.assertEqual(t.count('a'), 2)
        self.assertEqual(t.count('ab'), 1)

if __name__ == '__main__':
    unittest.main()
