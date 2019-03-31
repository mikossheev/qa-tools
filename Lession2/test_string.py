"""Here are the tests with string"""
TEST_STRING = "Some text here"


def test_end_string(string_prepare, before_type, before_all):
    """Does the string, prepared in the fixture have 'here' on its end?"""
    assert string_prepare.endswith("here")


def test_string_length_and_space(string_prepare):
    """Does the string consist of 26 characters and starts not with space?"""
    assert len(string_prepare) == 26
    assert not string_prepare.startswith(" ")
