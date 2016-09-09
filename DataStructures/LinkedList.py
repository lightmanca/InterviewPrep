from DataStructures.LinkedListNode import LinkedListNode
from DataStructures.LinkedStack import LinkedStack


class LinkedList:
    head = None
    count = 0

    def __init__(self, initial_list=None):
        if initial_list is not None:
            for e in initial_list:
                self.add_item_bottom(e)

    def add_item_bottom(self, data):
        new_node = LinkedListNode(data)
        self.count += 1
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def add_item_top(self, data):
        new_node = LinkedListNode(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_item_at_index(self, index, data):
        new_node = LinkedListNode(data)
        self.count += 1
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        prev = None
        for i in range(0, index):
            prev = node
            node = node.next
            if node is None:
                break
        if prev:
            prev.next = new_node
        else:
            self.head = new_node
        if node:
            new_node.next = node

    def rev_num_items_in_list(self, number_items_to_reverse):
        if number_items_to_reverse >= self.count:
            return False
        stack = LinkedStack()
        node = self.head
        for i in range(0, number_items_to_reverse):
            stack.push(node.value)
            if node.next is not None:
                node = node.next
        rest_of_list = node
        print("Stack:  ")
        stack.print_list()
        self.head = None
        prev = None
        while True:
            node = LinkedListNode(stack.pop())
            if self.head is None:
                self.head = node
                prev = node
            else:
                prev.next = node
                prev = node
            if stack.is_empty():
                break
        prev.next = rest_of_list
        return True

    def remove_item_matching(self, data):
        if self.is_empty():
            return False
        prev = None
        node = self.head
        while node.value != data and node.next is not None:
            prev = node
            node = node.next
        if node.value != data:
            # data item not found in list
            return False
        if prev:
            if node.next:
                prev.next = node.next
            else:
                prev.next = None
        else:
            if node.next:
                self.head = node.next
            else:
                self.head = None
        self.count -= 1
        return True

    def remove_item_at_index(self, index):
        if index >= self.count:
            # index greater than # of items in list.
            return False
        prev = None
        node = self.head
        for i in range(0, index):
            prev = node
            node = node.next
        if prev:
            if node.next:
                prev.next = node.next
            else:
                prev.next = None
        else:
            if node.next:
                self.head = node.next
            else:
                self.head = None
        self.count -= 1
        return True

    def is_empty(self):
        return self.count == 0

    def make_array_from_list(self):
        array = []
        node = self.head
        while node:
            array.append(node.value)
            node = node.next
        return array

    def verify_list_integrity(self):
        pass

    def print_list(self):
        print("List: {}".format(self.make_array_from_list()))
