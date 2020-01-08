import random
import string
import unittest

class Treap:
    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, key):
        prev = None
        curr = self.root

        while curr:
            if key == curr.key:
                break

            prev = curr
            if key < curr.key:
                curr = curr.lo
            else:
                curr = curr.hi

        return prev, curr

    def __getitem__(self, key):
        prev, curr = self.find(key)
        if curr:
            return curr.val

    def __setitem__(self, key, val):
        node = Node(key, val)

        if self.root == None:
            self.root = node
            return

        prev, curr = self.find(key)

        if curr:
            curr.val = val
            return

        if key < prev.key:
            prev.lo = node
            node.hi_parent = prev
        else:
            prev.hi = node
            node.lo_parent = prev
        self.bubble_up(node)

    def bubble_up(self, curr):
        if curr.lo_parent and curr.priority < curr.lo_parent.priority:
            curr = self.rotate_lo(curr.lo_parent)
            self.bubble_up(curr)
        elif curr.hi_parent and curr.priority < curr.hi_parent.priority:
            curr = self.rotate_hi(curr.hi_parent)
            self.bubble_up(curr)

    def rotate_lo(self, curr):
        next = curr.hi
        next.lo_parent = curr.lo_parent
        next.hi_parent = curr.hi_parent

        if next.lo_parent:
            next.lo_parent.hi = next
        elif next.hi_parent:
            next.hi_parent.lo = next
        else:
            self.root = next

        temp = next.lo
        next.lo = curr
        curr.lo_parent = None
        curr.hi_parent = next
        curr.hi = temp
        if temp:
            temp.lo_parent = curr
            temp.hi_parent = None
        return next

    def rotate_hi(self, curr):
        next = curr.lo
        next.lo_parent = curr.lo_parent
        next.hi_parent = curr.hi_parent

        if next.lo_parent:
            next.lo_parent.hi = next
        elif next.hi_parent:
            next.hi_parent.lo = next
        else:
            self.root = next

        temp = next.hi
        next.hi = curr
        curr.lo_parent = next
        curr.hi_parent = None
        curr.lo = temp
        if temp:
            temp.lo_parent = None
            temp.hi_parent = curr
        return next

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
        self.priority = random.random()

        self.lo_parent = None
        self.hi_parent = None
        self.lo = None
        self.hi = None


class TestTreap(unittest.TestCase):
    def is_sorted(self, treap):
        order = treap.get_preorder()
        order = list(map(lambda x: x.key, order))
        self.assertEqual(order, sorted(order))

    def is_prioritized(self, treap):
        def recurse(curr):
            if curr.lo:
                if curr.priority > curr.lo.priority or not recurse(curr.lo):
                    return False
            if curr.hi:
                if curr.priority > curr.hi.priority or not recurse(curr.hi):
                    return False
            return True
        self.assertTrue(recurse(treap.root))

    def test_getitem(self):
        treap = Treap()
        treap['key'] = 'val'
        self.assertEqual(treap['key'], 'val')

    def test_insert(self):
        for _ in range(100):
            treap = Treap()
            for _ in range(10):
                key = random.choice(string.ascii_uppercase)
                treap[key] = None
            self.is_sorted(treap)
            self.is_prioritized(treap)

if __name__ == '__main__':
    unittest.main()
