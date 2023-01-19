_ones = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']

_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


_tens = ['twenty', 'thirty', 'forty', 'fifty',
         'sixty', 'seventy', 'eighty', 'ninety']


def number_to_words(number: int) -> str:
    if number < 10:
        return _ones[number]

    if number < 20:
        return _teens[number - 10]

    if number < 100:
        tens = number // 10 - 2
        ones = number % 10
        return f"{_tens[tens]} {_ones[ones]}" if ones else _tens[tens]
