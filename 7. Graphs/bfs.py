# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        ans = []
        while queue:
            v = queue.pop(0)
            ans.append(v.name)
            for child in v.children:
                queue.append(child)
        return ans
