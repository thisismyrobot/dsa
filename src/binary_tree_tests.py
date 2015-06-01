""" Tests of binary tree implementation.

    "BT" is used here for Binary Tree, *not* BTree.
"""
import binary_tree
import unittest


class TestBinaryTrees(unittest.TestCase):
    """ Tests of binary tree.
    """
    def test_creation(self):
        """ Test the creation of a list.
        """
        bt = binary_tree.BinaryTree()

        # The BT has an empty root node
        self.assertIs(bt.root_node, None)

        # But we can create one with a root node.
        bt = binary_tree.BinaryTree(binary_tree.Node('g'))

        self.assertEquals(bt.root_node.data, 'g')

    def test_population(self):
        """ We have a helper to populate the tree.
        """
        bt = binary_tree.BinaryTree()

        bt.populate(['g', 'b', 't', 'z', 'c'])

        self.assertEquals(bt.root_node.data, 'g')

        self.assertEquals(bt.root_node.left.data, 'b')

        self.assertEquals(bt.root_node.left.right.data, 'c')

    def test_inorder(self):
        """ We print with an inorder representation.
        """
        bt = binary_tree.BinaryTree()

        bt.populate(['g', 'b', 't', 'z', 'c'])

        self.assertEquals(bt.inorder(bt.root_node), ['b', 'c', 'g', 't', 'z'])

        self.assertEquals(bt.__str__(), 'b c g t z')


if __name__ == '__main__':
    unittest.main()
