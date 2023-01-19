from src.converter import number_to_words


def test_single_digit_number_to_word():
    assert number_to_words(1) == 'one'
    assert number_to_words(5) == 'five'


def test_teens_to_words():
    assert number_to_words(11) == 'eleven'
    assert number_to_words(12) == 'twelve'
    assert number_to_words(15) == 'fifteen'
