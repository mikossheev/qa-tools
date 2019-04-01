"""Here are some test preparations"""
import random
import string

import pytest

TEST_STRING_PART_START = "Some random text "
TEST_STRING_PART_END = " here"


@pytest.fixture(scope="session")
def session_min_random_number():
    """This function defines the minimum number for all the random operations in the session"""
    number = random.randint(1, 4)
    print('The minimum number of session is ' + str(number))
    return number


@pytest.fixture(scope="module")
def random_number(session_min_random_number):
    """This function defines the main random number used in the module"""
    number = random.randint(session_min_random_number, 10)
    print('The main number of module is ' + str(number))
    return number


@pytest.fixture(scope="function")
def random_prepare(random_number):
    """This function defines a random string,
    which is used as a basic object in different tests"""
    rnd = "" + ''.join(random.
                       choices(string.ascii_uppercase, k=random_number))
    print('The random string for the current test is ' + rnd)
    return rnd


@pytest.fixture()
def string_prepare(random_prepare):
    """This function defines a string from random and preset parts"""
    string_for_current_test = \
        TEST_STRING_PART_START + random_prepare + TEST_STRING_PART_END
    yield string_for_current_test


@pytest.fixture()
def list_prepare(random_prepare, random_number, session_min_random_number):
    """This function defines a list, generated from random string"""
    list_for_current_test = [list_for_current_test *
                             random.randint(session_min_random_number, random_number)
                             for list_for_current_test in random_prepare]
    print('The random list for the current test is ' + list_for_current_test.__str__())
    return list_for_current_test
