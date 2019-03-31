"""Here are some test preparations"""
import random
import string

import pytest

NUMBER_OF_RANDOM_SYMBOLS = 4
TEST_STRING_PART_START = "Some random text"
TEST_STRING_PART_END = " here"


@pytest.fixture(scope="function")
def string_prepare():
    test_string_random_part = " " + ''.join(random.choices
                                            (string.ascii_uppercase, k=NUMBER_OF_RANDOM_SYMBOLS))
    string_for_current_test = \
        TEST_STRING_PART_START + test_string_random_part + TEST_STRING_PART_END
    print('\nStart execution of a test with >>>' + string_for_current_test + "<<<")
    yield string_for_current_test


@pytest.fixture(scope="module")
def random_text_length():
    print('\nStart execution of string tests with ' + str(NUMBER_OF_RANDOM_SYMBOLS) + " random symbols")
    yield NUMBER_OF_RANDOM_SYMBOLS


@pytest.fixture(scope="session")
def before_all():
    print('\nStart execution of all tests')


