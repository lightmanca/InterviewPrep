import pytest

from Tree import Tree


class TestClass:
    def setup_class(self):
        pass

    def test_tree(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        tree.print_tree()
        assert True

    def test_compare_trees(self):
        tree1 = Tree()
        tree2 = Tree()
        assert tree1.compare_tree(tree2) is True
        tree1.add(3)
        assert tree1.compare_tree(tree2) is False
        tree1.add(4)
        tree1.add(0)
        tree1.add(8)
        tree1.add(2)

        tree2.add(3)
        tree2.add(4)
        tree2.add(0)
        tree2.add(8)
        tree2.add(2)
        assert tree1.compare_tree(tree2) is True

        tree2.add(10)
        assert tree1.compare_tree(tree2) is False

        tree1.add(10)
        assert tree1.compare_tree(tree2) is True

        tree1.add(-1)
        assert tree1.compare_tree(tree2) is False

        tree2.add(-1)
        assert tree1.compare_tree(tree2) is True

        tree1.add(-5)
        tree2.add(-3)
        assert tree1.compare_tree(tree2) is False

        tree2.add(-5)
        tree1.add(-3)
        tree1.print_tree()
        # tree2.rebalance_tree()
        #tree1.rebalance_tree()
        #tree1.print_tree()
        # assert tree1.compare_tree(tree2) is True
