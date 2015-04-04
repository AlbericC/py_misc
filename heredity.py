
class Heredity():
    def __init__(self):
        """Provides heredity capability

        Suitable for any n/n "hierarchic" structure,
        methods:
        add_parent(other)
        add_child(other)
        has_parent(other)
        has_child(other)"""

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

    def ancestors(self):
        if self.parent:
            return set.union(self.parent, *(a.ancestors() for a in self.parent))
        else:
            return set()

    def descendants(self):
        if self.child:
            return set.union(self.child, *(a.descendants() for a in self.parent))
        else:
            return set()