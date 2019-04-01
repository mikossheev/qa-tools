"""Here are the tests with lists"""
import random


def test_list_length_and_space(list_prepare, random_number, session_min_random_number):
    """Test checks the length of the list, depending on random number of the session,
    and that the length of the random element of the list is between minimum and random number"""
    assert len(list_prepare) == random_number
    assert len(list_prepare[random.randint(1, random_number)]) >= session_min_random_number


def test_list_sort(list_prepare, random_number):
    list_prepare.sort(key=len)
    assert len(list_prepare[0]) <= len(list_prepare[int(random_number)-1])
