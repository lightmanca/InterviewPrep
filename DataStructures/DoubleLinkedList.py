from DataStructures.LinkedListNode import LinkedListNode
from DataStructures.LinkedStack import LinkedStack


class DoubleLinkedList:
    head = None
    tail = None
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
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def add_item_top(self, data):
        new_node = LinkedListNode(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def add_item_at_index(self, index, data):
        new_node = LinkedListNode(data)
        self.count += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
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
            new_node.prev = prev
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        if node:
            node.prev = new_node
            new_node.next = node
        else:
            self.tail = new_node



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
            new_node = LinkedListNode(stack.pop())
            if self.head is None:
                self.head = new_node
                prev = new_node
            else:
                prev.next = new_node
                new_node.prev = prev
                prev = new_node
            if stack.is_empty():
                break
        prev.next = rest_of_list
        rest_of_list.prev = prev
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
                node.next.prev = prev
            else:
                prev.next = None
                self.tail = prev
        else:
            if node.next:
                self.head = node.next
                node.next.prev = None
            else:
                self.head = None
                self.tail = None
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
            if not node.next:
                break
            node = node.next
        if prev:
            if node.next:
                prev.next = node.next
                node.next.prev = prev
            else:
                prev.next = None
        else:
            if node.next:
                self.head = node.next
                node.next.prev = prev
            else:
                self.head = None
                self.tail = None
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
        list_forwards = self.make_array_from_list()
        list_backwards = []
        node = self.tail
        while node:
            list_backwards.insert(0, node.value)
            node = node.prev
        assert list_forwards == list_backwards

    def print_list(self):
        print("List: {}".format(self.make_array_from_list()))
