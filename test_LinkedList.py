from DataStructures.LinkedList import LinkedList
from LinkedListTestBase import LinkedListBase


class TestLinkedList(LinkedListBase):
    def setup_class(self):
        print("Linked list tests")
        self.makeLinkedList = lambda self, initial_data=None: LinkedList(initial_data)
