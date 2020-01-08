import random
import string
import unittest

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, key):
        prev, curr = None, self.root
        while curr:
            if key == curr.key:
                break
            if key < curr.key:
                prev, curr = curr, curr.lo
            else:
                prev, curr = curr, curr.hi
        return prev, curr

    def insert(self, node):
        if self.root:
            prev, curr = self.find(node.key)
            if curr:
                curr.val = node.val
            else:
                if key < prev.key:
                    prev.lo = node
                else:
                    prev.hi = node
                node.parent = prev
        else:
            self.root = node

    def __getitem__(self, key):
        curr = self.find(self.root, key)
        if curr:
            return curr.val

    def __setitem__(self, key, val):
        node = Node(key, val)
        self.insert(node)

    def get_preorder(self):
        def recurse(curr):
            if curr == None:
                return []
            return recurse(curr.lo) + [curr] + recurse(curr.hi)
        return recurse(self.root)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.parent = None
        self.lo = None
        self.hi = None


class TestBST(unittest.TestCase):
    def is_sorted(self, bst):
        order = bst.get_preorder()
        order = list(map(lambda x: x.key, order))
        self.assertEqual(order, sorted(order))

    def test_getitem(self):
        bst = BST()
        bst['key'] = 'val'
        self.assertEqual(bst['key'], 'val')

    def test_setitem(self):
        for _ in range(100):
            bst = Treap()
            for _ in range(10):
                key = random.choice(string.ascii_uppercase)
                bst[key] = None
            self.is_sorted(bst)

if __name__ == '__main__':
    unittest.main()
