import random


def test_dict_has_duplicates():
    """This test checks that there are no duplicates in dict"""
    test_dict = {"first": 1, "second": 2}
    test_dict["first"] = 3
    assert test_dict["first"] != 1


def test_dict_new_item(random_number):
    """This test checks that new value is added to the dictionary,
    and deleted after .popitem"""
    test_dict = {k: random.random() for k in range(random_number)}
    test_dict[random_number+1] = "test"
    assert test_dict.popitem() == (int(random_number+1), "test")
    assert len(test_dict) == random_number
