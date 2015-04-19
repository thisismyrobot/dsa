import singly_linked_list
import unittest


class TestSinglyLinkedLists(unittest.TestCase):
    """ Tests of singly-linked-lists.
    """
    def test_creation(self):
        """ Test the creation of a list.
        """
        sl_list = singly_linked_list.SinglyLinkedList()

        # The list starts off with no Node - this is an empty list.
        self.assertIs(sl_list.node, None)


if __name__ == '__main__':
    unittest.main()
