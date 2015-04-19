""" A singly-linked-list implementation in Python.
"""

class Node(object):
    """ The proverbial Node.

        Based initially on: http://stackoverflow.com/a/283630/577190
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self): 
        return str(self.data)


class SinglyLinkedList(object):
    """ The list itself.
    """
    def __init__(self, node=None):
        self.node = node

    @staticmethod
    def insert_after(node, new_node):
        """ Insert a node after a given node.

            Points the new_node's 'next' to the node following the given node,
            then points the given node's 'next' to the new node.
        """
        new_node.next = node.next
        node.next = new_node
