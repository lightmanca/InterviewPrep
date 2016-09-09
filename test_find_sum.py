def find_sum(int_set, target_sum):
    print("\nStart new")
    # int_set[0], iterate through rest of list to see if sum = 8
    if len(int_set) == 0:
        return False
    if len(int_set) == 1:
        if int_set[0] == target_sum:
            return True
        else:
            return False
    for x in range(0, len(int_set) - 1):
        sum = int_set[x]
        if sum == target_sum:
            return True
        end = len(int_set)
        for y in range(x + 1, end):
            sum = sum + int_set[y]
            print("x: {}, y: {}, sum: {}".format(x, y, sum))
            if sum == target_sum:
                return True
    return False


def test_find_sum():
    assert find_sum([1], 8) is False
    assert find_sum([8], 8) is True
    assert find_sum([0, 8], 8) is True
    assert find_sum([9, -1], 8) is True
    assert find_sum([-1, 9], 8) is True
    assert find_sum([-1, -1, 10], 8) is True
    assert find_sum([1, -1, -2, 3, 1, 4, -4], 8) is True
