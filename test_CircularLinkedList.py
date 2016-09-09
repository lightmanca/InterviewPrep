from DataStructures.CircularLinkedList import CircularLinkedList
from LinkedListTestBase import LinkedListBase


class TestCircularList(LinkedListBase):
    def setup_class(self):
        print("Circular linked list Tests")
        self.makeLinkedList = lambda self, initial_data=None: CircularLinkedList(initial_data)
