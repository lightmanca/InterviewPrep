import pytest


def match_brackets(input):
    bracket_match = {'}': '{', ']': '[', ')': '('}
    bracket_list = []
    if input == "":
        return False
    for c in input:
        if c in bracket_match.values():
            bracket_list.append(c)
        if c in bracket_match.keys():
            if bracket_match[c] in bracket_list:
                bracket_list.remove(bracket_match[c])
            else:
                return False
    return len(bracket_list) == 0


def test_match_bracket():
    print("Match Brackets")
    assert match_brackets("") is False
    assert match_brackets("{[()]}") is True
    assert match_brackets("{[()]}(") is False
    assert match_brackets("{[()}]") is True
    assert match_brackets("([()}]") is False
    assert match_brackets("(((([[[[))))]]]]") is True
