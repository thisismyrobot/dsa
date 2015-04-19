""" A singly-linked-list implementation in Python.
"""

class Node(object):
    """ The proverbial Node.

        Based initially on: http://stackoverflow.com/a/283630/577190
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList(object):
    """ The list itself.
    """
    def __init__(self, first_node=None):
        self.first_node = first_node

    def __str__(self):
        data = []
        n = self.first_node
        while n:
            data.append(n.data)
            n = n.next_node
        return ', '.join(map(str, data))

    @staticmethod
    def insert_after(node, new_node):
        """ Insert a node after a given node.

            Points the new_node's 'next_node' to the node following the given
            node, then points the given node's 'next_node' to the new node.
        """
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_beginning(self, new_node):
        """ Insert a new node at the beginning.

            Point the new_node's 'next_node' to the current root node, update
            the root node to be the new_node.
        """
        new_node.next_node = self.first_node
        self.first_node = new_node

    @staticmethod
    def remove_after(node):
        """ Remove the node after a node.

            Sets the 'next_node' of the node to be the 'next_node' of the next
            node, assuming the next node is not None.
        """
        if node.next_node:
            node.next_node = node.next_node.next_node

    def remove_beginning(self):
        """ Remove the first node.

            Sets the first_node node to be the value of the first_node's next.
        """
        self.first_node = self.first_node.next_node

    def append(self, new_node):
        """ Append a node to the end of the linked list.

            Traverse to the end, replace the last node's 'next_node' with the
            passed in node.
        """
        n = self.first_node

        if n is None:
            self.insert_beginning(new_node)
            return

        while n.next_node:
            n = n.next_node

        self.insert_after(n, new_node)

    def delete(self, node):
        """ Delete a node, ignore missing node.

            TODO: clarify behaviour around missing nodes.
        """
        n = self.first_node

        if n is None:
            return

        while n.next_node is not node:
            n = n.next_node

            # Handle reaching end without finding node
            if n is None:
                return

        self.remove_after(n)
