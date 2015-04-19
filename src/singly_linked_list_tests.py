""" Tests of singly-linked-lists.
"""
from singly_linked_list import SinglyLinkedList, Node
import unittest


class TestSinglyLinkedLists(unittest.TestCase):
    """ Tests of singly-linked-lists.
    """
    def test_creation(self):
        """ Test the creation of a list and the fundamental object attributes.
        """
        sll = SinglyLinkedList()

        # The list starts off with no 'first' Node - this is an empty list.
        self.assertIs(sll.first_node, None)

        # We can create a list with 'first_node' populated.
        sll = SinglyLinkedList(Node('hello'))

        self.assertEquals(sll.first_node.data, 'hello')

    def test_removals(self):
        """ Test list removals.
        """
        node1 = Node('first')
        sll = SinglyLinkedList(node1)

        node2 = Node('second')
        sll.insert_after(node1, node2)

        self.assertEquals(str(sll), 'first, second')

        sll.remove_after(node1)

        self.assertEquals(str(sll), 'first')

        sll.insert_after(node1, node2)

        sll.remove_beginning()

        self.assertEquals(str(sll), 'second')

    def test_inserts(self):
        """ Test list inserts.
        """
        sll = SinglyLinkedList(Node('first'))

        sll.insert_after(sll.first_node, Node('second'))

        self.assertEquals(sll.first_node.data, 'first')

        self.assertEquals(sll.first_node.next_node.data, 'second')

        sll.insert_beginning(Node('before the first'))

        self.assertEquals(sll.first_node.data, 'before the first')

        self.assertEquals(sll.first_node.next_node.data, 'first')

        self.assertEquals(sll.first_node.next_node.next_node.data, 'second')

        self.assertEquals(str(sll), 'before the first, first, second')

    def test_append(self):
        """ Test an append method.
        """
        sll = SinglyLinkedList()
        sll.append(Node('first'))
        sll.append(Node('second'))
        sll.append(Node('third'))
        self.assertEquals(str(sll), 'first, second, third')

    def test_delete(self):
        """ Test a delete method.
        """
        sll = SinglyLinkedList()
        node1, node2, node3 = Node(1), Node(2), Node(3)

        sll.append(node1)
        sll.append(node2)
        sll.append(node3)

        self.assertEquals(str(sll), '1, 2, 3')

        sll.delete(node2)

        self.assertEquals(str(sll), '1, 3')

        # It silently handles missing items
        sll.delete(Node(4))

        self.assertEquals(str(sll), '1, 3')

    def test_print(self):
        """ Test the list printing.
        """
        sll = SinglyLinkedList(Node('first'))
        sll.insert_after(sll.first_node, Node('second'))
        self.assertEquals(str(sll), 'first, second')


if __name__ == '__main__':
    unittest.main()
