#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):

        if type(data) is not int:
            raise TypeError("data must be an integer")
        if (next_node and type(next_node) != Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if (value and type(value) != Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    __head = None
    def __init__(self):
        pass

    def sorted_insert(self, value):
        my_new_node = Node(value)
        if (SinglyLinkedList.__head is None):
            SinglyLinkedList.__head = my_new_node
        else:
            SinglyLinkedList.temp = SinglyLinkedList.__head
            if (SinglyLinkedList.temp.data > my_new_node.data):
                my_new_node.next_node(SinglyLinkedList.temp)
                SinglyLinkedList.__head = my_new_node
                return
            while (SinglyLinkedList.temp and SinglyLinkedList.temp.next_node):
                if SinglyLinkedList.temp.next_node.data > my_new_node.data:
                    my_new_node.next_node(SinglyLinkedList.temp.next_node)
                    SinglyLinkedList.temp.next_node(my_new_node)
                    return
                else:
                    SinglyLinkedList.temp = SinglyLinkedList.temp.next_node
            SinglyLinkedList.temp.next_node(my_new_node)

    def __str__(self):
        string = str(SinglyLinkedList.__head.data)
        SinglyLinkedList.temp = SinglyLinkedList.__head.next_node
        while (SinglyLinkedList.temp):
            string += '\n' + str(SinglyLinkedList.temp.data)
            SinglyLinkedList.temp = SinglyLinkedList.temp.next_node 
        return string
