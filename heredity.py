
class Heredity():
    def __init__(self):
        """Provides heredity capability

        Suitable for any n/n "hierarchic" structure,
        """
        self._parent = set()
        self._child = set()

    def add_parent(self, parent):
        self._parent.add(parent)
        if not parent.has_child(self):
            parent.add_child(self)

    def add_child(self, child):
        self._child.add(child)
        if not child.has_parent(self):
            child.add_parent(self)

    def has_parent(self, other):
        return other in self._parent

    def has_child(self, other):
        return other in self._child

    @property
    def child(self):
        return self._child
    @property
    def parent(self):
        return self._parent

    def ancestors(self, depth="inf"):
        if self.parent and depth == "inf":
            return set.union(self.parent, *(a.ancestors(depth) for a in self.parent))
        elif self.parent and depth:  # an int for the depth has been given.
            return set.union(self.parent, *(a.ancestors(int(depth)-1) for a in self.parent))
        else:
            return set()

    def descendants(self, depth="inf"):
        if self.child and depth == "inf":
            return set.union(self.child, *(a.descendants(depth) for a in self.child))
        if self.child and depth:
            return set.union(self.child, *(a.descendants(int(depth)-1) for a in self.child))
        else:
            return set()

    def siblings(self):
        return set.union(*(a.child for a in self.parent))
        # set.union(*(a.parent for a in self.child)))