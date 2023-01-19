_digits = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']

_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def number_to_words(number: int) -> str:
    if number < 10:
        return _digits[number]

    return _teens[number - 10]
