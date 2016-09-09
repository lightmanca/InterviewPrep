from DataStructures.LinkedStack import LinkedStack


class TestStack:

    def test_push(self):
        print("\nTest Push")
        stack = LinkedStack()
        for x in [-1, -2, 0, 5, -10, 20]:
            stack.push(x)
        stack.print_list()
        assert stack.make_array_from_list() == [20, -10, 5, 0, -2, -1]

    def test_pop(self):
        print("\nTest Pop")
        stack = LinkedStack()
        for x in [-1, -2, 0, 5, -10, 20]:
            stack.push(x)
        stack.print_list()
        data = stack.pop()
        assert data == 20
        stack.print_list()
        assert stack.make_array_from_list() == [-10, 5, 0, -2, -1]

    def test_remove_item(self):
        print("\nTest Remove Item")
        stack = LinkedStack()
        for x in [-1, -2, 0, 5, -10, 20]:
            stack.push(x)
        stack.print_list()
        stack.remove_item(0)
        stack.print_list()
        assert stack.make_array_from_list() == [20, -10, 5, -2, -1]
