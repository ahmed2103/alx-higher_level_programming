#!/usr/bin/python3
""" Module providing a 'Node' class for a singly-linked list
"""


class Node:
    """ Definition of a singly-linked list node
    """
    def __init__(self, data, next_node=None):
        """ Instantiate a node
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """ Definition of a singly-linked list
    """
    def __init__(self):
        """ Instantiate a singly-linked list
        """
        self.head = None

    def __str__(self):
        """ Generate a visual representation of a list
        """
        if self.head is None:
            return "Empty list"

        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " -> "
            current = current.next_node
        result += "None"
        return result

    def sorted_insert(self, value):
        """ Insert a Node into a list sorted in ascending order
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
