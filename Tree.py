#!/usr/bin/python


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    @property
    def root_node(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            self._find(value, node.left)
        elif value > node.value and node.right is not None:
            self._find(value, node.right)

    def rebalance_tree(self):
        if self.root is None:
            return
        tree_list = self.get_tree_values()
        new_tree = Tree()
        self._rebalance_tree(tree_list, new_tree)
        self.root = new_tree.root

    def _rebalance_tree(self, tree_list, new_tree):
        # find the middle.
        if len(tree_list) == 0:
            return
        tree_middle = int(len(tree_list) / 2)
        print("Tree list :  {}, Tree middle: {}".format(tree_list, tree_middle))

        new_tree.add(tree_list[tree_middle - 1])
        new_tree.add(tree_list[tree_middle])
        new_tree.print_tree()

        # make 2 lists, one for left and right.
        if len(tree_list) <= 2:
            return
        tree_list_left = tree_list[0:tree_middle - 1]
        tree_list_right = tree_list[tree_middle:len(tree_list) + 1]
        self._rebalance_tree(tree_list_left, new_tree)
        self._rebalance_tree(tree_list_right, new_tree)

    def compare_tree(self, tree_to_compare):
        if self.root is None and tree_to_compare.root is None:
            return True
        return self._compare_tree(self.root, tree_to_compare.root)

    def _compare_tree(self, node1, node2):
        if self._compare_node(node1, node2) is False:
            return False
        if node1.right:
            if self._compare_tree(node1.right, node2.right) is False:
                return False
        if node1.left:
            if self._compare_tree(node1.left, node2.left) is False:
                return False
        return True

    @staticmethod
    def _compare_node(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        if (node1.right is None) != (node2.right is None):
            return False
        if (node1.left is None) != (node2.left is None):
            return False
        return True

    def delete_tree(self):
        # garbage collector will do this for us.
        self.root = None

    def print_tree(self):
        if self.root is not None:
            tree_values = self.get_tree_values()
            print("Tree: {}".format(tree_values))
        else:
            print("Tree is empty")

    def get_tree_values(self):
        tree_list = []
        if self.root is not None:
            self._get_tree_values(self.root, tree_list)
        return tree_list

    def _get_tree_values(self, node, tree_list):
        if node is not None:
            self._get_tree_values(node.left, tree_list)
            tree_list.append(node.value)
            self._get_tree_values(node.right, tree_list)
