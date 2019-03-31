"""Here are the tests with string"""
TEST_STRING = "Some text here"


def test_all_parts(string_prepare, before_type, before_all):
    """This test checks if the string starts with known start and end parts,
    and whether random part consists of letters in upper case"""
    test_string = string_prepare
    start_of_the_string = "Some random text "
    end_of_the_string = " here"

    assert test_string.startswith(start_of_the_string)
    test_string = test_string.lstrip(start_of_the_string)

    assert test_string.endswith(end_of_the_string)
    test_string = test_string.rstrip(end_of_the_string)

    assert test_string.isupper()
    assert test_string.isalpha()


def test_string_length_and_space(string_prepare):
    """Does the string, prepared in the fixture consist of 26 characters and starts not with space?"""
    assert len(string_prepare) == 26
    assert not string_prepare.startswith(" ")
