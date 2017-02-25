class Tree:

    def __init__(self, n=1):
        self.n = n
        self.array = [None] * (n)

    def add_elem(self, ind, val):
        self.array[ind] = val

    def get_parent(self, ind):
        parent = self.array[ind].parent
        return self.array[parent]

    def get_children(self, val):
        children = []
        for token in self.array:
            if token.parent == val:
                children.append(token)
        return children

    def get_root(self):
        for token in self.array:
            if token.parent == -1:
                return token

    def get_all_children(self, val):
        all_children = []
        stack = self.get_children(val)
        while stack:
            first = stack.pop(0)
            all_children.append(first)
            children = self.get_children(first.number)
            if children:
                for ch in children: stack.append(ch)
        return all_children
