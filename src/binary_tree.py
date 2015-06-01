""" A binary tree implementation.
"""


class Node(object):
    """ A binary tree node.
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BinaryTree(object):

    def __init__(self, root_node=None):
        self.root_node = root_node

    def insert(self, data):
        node = Node(data)

        if self.root_node is None:
            self.root_node = node
            return

        # Walk the tree and insert/replace
        cursor = self.root_node

        while True:
            if node.data < cursor.data:
                if cursor.left:
                    cursor = cursor.left
                    continue
                cursor.left = node
                break
            elif node.data > cursor.data:
                if cursor.right:
                    cursor = cursor.right
                    continue
                cursor.right = node
                break
            else:
                cursor = node

    def populate(self, data_items):

        self.root_node = None

        for data in data_items:
            self.insert(data)

    def inorder(self, node, result=None):
        """ Recursive in-order traversal.
        """
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result

    def __str__(self):
        """ Return an inorder representation of the tree.
        """
        result = self.inorder(self.root_node)
        return ' '.join(result)
