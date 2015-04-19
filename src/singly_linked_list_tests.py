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

    def test_print(self):
        """ Test the list printing.
        """
        sll = SinglyLinkedList(Node('first'))
        sll.insert_after(sll.first_node, Node('second'))
        self.assertEquals(str(sll), 'first, second')


if __name__ == '__main__':
    unittest.main()
