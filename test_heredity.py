#! /usr/bin/env python
import unittest

from heredity import Heredity


class HeredityTest(unittest.TestCase):
    def test_add_parent(self):
        child = Heredity()
        parent = Heredity()

        child.add_parent(parent)

        self.assertIn(parent, child.parent)
        self.assertIn(child, parent.child)

    def test_add_child(self):
        child = Heredity()
        parent = Heredity()

        parent.add_child(child)

        self.assertIn(child, parent.child)
        self.assertIn(parent, child.parent)

    def test_multiple_children(self):
        parent = Heredity()
        children = [Heredity() for i in range(5)]
        for child in children:
            parent.add_child(child)
        self.assertEqual(parent.child, set(children))
        for child in children[1:]:
            self.assertEqual(child.parent, children[0].parent)  # check that very children have the same parent

    def test_family_tree(self):
        l = [Heredity() for _ in range(10)]
        for idx, p in enumerate(l[:-1]):
            p.add_parent(l[idx+1])

        self.assertEqual(set(l), l[3].family_tree())


if __name__ == '__main__':
    unittest.main()