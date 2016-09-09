from DataStructures.LinkedListNode import LinkedListNode


class LinkedStack:
    head = None
    num_items = 0

    def __init__(self, initial_stack=None):
        # if you specify an initial stack items will be pushed from left to right.
        if initial_stack:
            for item in initial_stack:
                self.push(item)
        pass

    def push(self, data):
        node = LinkedListNode(data)
        if self.head:
            node.next = self.head
        self.head = node
        self.num_items += 1

    def pop(self):
        if self.num_items == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_items -= 1
        return value

    def is_empty(self):
        return self.num_items == 0

    def remove_item(self, item_to_remove):
        my_stack = LinkedStack()
        found = False
        while not self.is_empty():
            item = self.pop()
            if item == item_to_remove:
                found = True
                break
            my_stack.push(item)
        while not my_stack.is_empty():
            self.push(my_stack.pop())
        return found

    def make_array_from_list(self):
        array = []
        node = self.head
        while node:
            array.append(node.value)
            node = node.next
        return array

    def print_list(self):
        print("Stack: {}".format(self.make_array_from_list()))
