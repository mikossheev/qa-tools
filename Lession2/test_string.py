"""Here are the tests with string"""


def test_string_length_and_space(string_prepare, random_number):
    """Test checks the length of string, depending on random text length,
    and that string does not start with a space"""
    assert len(string_prepare) == 22 + random_number
    assert not string_prepare.startswith(" ")


def test_all_parts(string_prepare, random_number):
    """This test checks if the string starts with known start and end parts,
    and whether random part consists of letters in upper case"""

    start_of_the_string = "Some random text "
    end_of_the_string = " here"

    assert string_prepare.startswith(start_of_the_string)
    string_prepare = string_prepare.replace(start_of_the_string, "")

    assert string_prepare.endswith(end_of_the_string)
    string_prepare = string_prepare.replace(end_of_the_string, "")

    assert string_prepare.isupper()
    assert string_prepare.isalpha()

    assert len(string_prepare) == random_number


