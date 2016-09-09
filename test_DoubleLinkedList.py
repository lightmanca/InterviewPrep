from DataStructures.DoubleLinkedList import DoubleLinkedList
from LinkedListTestBase import LinkedListBase


class TestDoubleLinkedList(LinkedListBase):
    def setup_class(self):
        print("Double linked list Tests")
        self.makeLinkedList = lambda self, initial_data=None: DoubleLinkedList(initial_data)
