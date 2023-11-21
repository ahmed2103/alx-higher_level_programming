#!/usr/bin/python3

class Node:
    """ Definition of a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Instantiate a node with data and optional next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data stored in a node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Set the data stored in a node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieve the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Set the next node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Definition of a singly linked list
    """
    def __init__(self):
        """ Instantiate a singly linked list with head as None
        """
        self.head = None

    def __str__(self):
        """ Print the entire list in stdout
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """ Insert a new Node into the correct sorted position in the list (increasing order)
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
