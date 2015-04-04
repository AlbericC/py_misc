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

if __name__ == '__main__':
    unittest.main()