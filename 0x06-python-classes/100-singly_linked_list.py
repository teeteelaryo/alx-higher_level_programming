#!/usr/bin/python3
"""A singly linked list module"""


class Node:
    """A singly linked list Node class"""

    def __init__(self, data, next_node=None):
        """Initialized node data and node next sibling if any

            Args:
                data (int): The node data
                next_node (Node): A node instance
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """___data property getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """___data property setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """__next_node property getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """__next_node property setter"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """Initialize the head of the list"""
        self.__head = None

    def __str__(self):
        """Prints the value in the singly linked list"""
        node = self.__head
        text = ""
        if node:
            text = "{:d}".format(node.data)
            node = node.next_node
        while node:
            text += "\n{:d}".format(node.data)
            node = node.next_node
        return text

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list
            increasing order.

            Args:
                value (int): An integer
        """
        new_node = Node(value)
        cursor = self.__head
        tmp = None

        while cursor and value > cursor.data:
            tmp = cursor
            cursor = cursor.next_node

        new_node.next_node = cursor

        if not tmp:
            self.__head = new_node
        else:
            tmp.next_node = new_node
