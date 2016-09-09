class LinkedListBase:
    makeLinkedList = None

    def setup_class(self):
        self.makeLinkedList = lambda self, initial_data=None: []

    def test_make_list(self):
        print("Make list test")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5]
        list.verify_list_integrity()

    def test_add_item_below(self):
        print("Add Item below")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_bottom(10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5, 10]
        list.verify_list_integrity()

    def test_add_item_below_empty_list(self):
        print("Add Item below empty list")
        list = self.makeLinkedList()
        list.add_item_bottom(10)
        list.print_list()
        assert list.make_array_from_list() == [10]
        list.verify_list_integrity()

    def test_add_item_top(self):
        print("Add Item top")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_top(10)
        list.print_list()
        assert list.make_array_from_list() == [10, 1, 2, 3, 4, 5]
        list.verify_list_integrity()

    def test_add_item_top_empty_list(self):
        print("Add Item top empty list")
        list = self.makeLinkedList()
        list.add_item_top(10)
        list.print_list()
        assert list.make_array_from_list() == [10]
        list.verify_list_integrity()

    def test_add_item_at_index(self):
        print("Add Item At index")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_at_index(3, 10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 10, 4, 5]
        list.verify_list_integrity()

    def test_add_item_at_index_at_top_of_list(self):
        print("Add Item At index")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_at_index(0, 10)
        list.print_list()
        assert list.make_array_from_list() == [10, 1, 2, 3, 4, 5]
        list.verify_list_integrity()

    def test_add_item_at_index_item_at_end_of_list(self):
        print("Add Item At index item is at end of list")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_at_index(5, 10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5, 10]
        list.verify_list_integrity()

    def test_add_item_at_index_item_past_end_of_list(self):
        print("Add Item At index item is past end of list")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.add_item_at_index(10, 10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5, 10]
        list.verify_list_integrity()

    def test_remove_item_matching(self):
        print("Remove item matching")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.remove_item_matching(3)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 4, 5]
        list.verify_list_integrity()

    def test_remove_item_matching_no_match(self):
        print("Remove item not matching")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.remove_item_matching(10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5]
        list.verify_list_integrity()

    def test_remove_item_matching_single_item_in_list(self):
        print("Remove item matching single item in list")
        list = self.makeLinkedList([5])
        list.remove_item_matching(5)
        list.print_list()
        assert list.make_array_from_list() == []
        list.verify_list_integrity()

    def test_remove_item_matching_empty_list(self):
        print("Remove item not matching")
        list = self.makeLinkedList()
        list.remove_item_matching(10)
        list.print_list()
        assert list.make_array_from_list() == []
        list.verify_list_integrity()

    # -------
    def test_remove_item_at_index(self):
        print("Remove item at Index")
        list = self.makeLinkedList([1, 2, 8, 4, 5])
        list.remove_item_at_index(2)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 4, 5]
        list.verify_list_integrity()

    def test_remove_item_at_index_0(self):
        print("Remove item at Index")
        list = self.makeLinkedList([1, 2, 8, 4, 5])
        list.remove_item_at_index(0)
        list.print_list()
        assert list.make_array_from_list() == [2, 8, 4, 5]
        list.verify_list_integrity()

    def test_remove_item_at_index_too_high(self):
        print("Remove item not matching")
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.remove_item_at_index(10)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5]
        list.verify_list_integrity()

    def test_remove_item_at_index_single_item(self):
        print("Remove item matching single item in list")
        list = self.makeLinkedList([5])
        list.remove_item_at_index(0)
        list.print_list()
        assert list.make_array_from_list() == []
        list.verify_list_integrity()

    def test_remove_item_at_index_empty_list(self):
        print("Remove item not matching")
        list = self.makeLinkedList()
        list.remove_item_matching(0)
        list.print_list()
        assert list.make_array_from_list() == []
        list.verify_list_integrity()

    def test_reverse_linked_list(self):
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.print_list()
        list.rev_num_items_in_list(4)
        list.print_list()
        assert list.make_array_from_list() == [4, 3, 2, 1, 5]
        list.verify_list_integrity()

    # I wasn't sure if this should reverse the list or not.  simply changing my statement
    # if self.count ==0 or self.count <= num_items:
    # to:
    # if self.count ==0 or self.count < num_items:
    # will allow this code to reverse the numbers as well.
    def test_reverse_linked_list_equal_length(self):
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.print_list()
        list.rev_num_items_in_list(5)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5]

    def test_reverse_linked_list_greater_length(self):
        list = self.makeLinkedList([1, 2, 3, 4, 5])
        list.print_list()
        list.rev_num_items_in_list(6)
        list.print_list()
        assert list.make_array_from_list() == [1, 2, 3, 4, 5]

    def test_reverse_linked_empty_list(self):
        list = self.makeLinkedList([])
        list.print_list()
        list.rev_num_items_in_list(0)
        list.print_list()
        assert list.make_array_from_list() == []

    def test_reverse_linked_list_different_values(self):
        list = self.makeLinkedList([8, 10, -1, 20, 15, 8, 5])
        list.print_list()
        list.rev_num_items_in_list(6)
        list.print_list()
        assert list.make_array_from_list() == [8, 15, 20, -1, 10, 8, 5]

    def test_reverse_linked_list_large_array(self):
        input_list_array = []
        reversed_list_array = []
        # create our input list
        for x in range(1, 2000, 2):
            input_list_array.append(x)
        # create our reversed list to compare to the input list.
        for x in range(999, 0, -2):
            reversed_list_array.append(x)
        for x in range(1001, 2000, 2):
            reversed_list_array.append(x)
        list = self.makeLinkedList(input_list_array)
        list.print_list()
        list.rev_num_items_in_list(500)
        list.print_list()
        print(reversed_list_array)
        assert list.make_array_from_list() == reversed_list_array
