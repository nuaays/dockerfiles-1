#! /usr/bin/env python3
import os
from subprocess import call

BASE_DIR = os.path.dirname(__file__)

class Node(object):
    def __init__(self, name, from_name):
        self.name = name
        self.from_name = from_name
        self.children = []
        self.parent = None

    def display(self, depth=0):
        print("\t" * depth, self.name, '-', self.from_name)
        for child in self.children:
            child.display(depth + 1)

    def walk(self):
        for child in self.children:
            yield child
            yield from child.walk()


class Tree(object):
    def __init__(self):
        self.branches = []

    def insert(self, node):
        # If there are no branches make this node a branch
        if not self.branches:
            self.branches.append(node)
            return

        # Check if any of the current branches depend on this node
        for index, branch in enumerate(self.branches):
            if branch.from_name == node.name:
                node.children.append(branch)
                del self.branches[index]

        # Find the parent node
        parent = self.search(node.from_name)

        # If there isn't a parent then make this a branch
        if parent is None:
            self.branches.append(node)
        else:
            # Make this a dependency of the parent
            parent.children.append(node)

    def walk(self):
        for branch in self.branches:
            yield branch
            yield from branch.walk()

    def search(self, name):
        for node in self.walk():
            if node.name == name:
                return node

        return None

    def display(self):
        for branch in self.branches:
            branch.display()


tree = Tree()


for dirpath, dirnames, filenames in os.walk(BASE_DIR):
    if ((dirpath.startswith('./.git')) or dirpath == '.' or
            'Dockerfile' not in filenames or
            'skip' in filenames):
        continue

    filename = os.path.join(dirpath, 'Dockerfile')
    with open(filename, 'r') as f:
        fromline = f.readline()

    if fromline.endswith("\n"):
        fromline = fromline[:-1]

    from_image = fromline[5:]

    if '@' in from_image:
        from_image, _ = from_image.split('@')
    elif ':' in from_image:
        from_image, _ = from_image.split(':')

    image = dirpath[2:]

    tree.insert(Node(image, from_image))

tree.display()

for node in tree.walk():
    name = node.name
    pathname = os.path.join(BASE_DIR, name)
    proc = call(["make -C " + pathname + " build"], shell=True)
