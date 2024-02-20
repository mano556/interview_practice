def number_to_words(number):
    words_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if number in words_dict:
        return words_dict[number]

    if number < 100:
        return words_dict[number // 10 *10 ] + '-' + words_dict[number % 10]

    if number < 1000:
        return words_dict[number // 100] + ' hundreden ' + number_to_words(number % 100)

    return 'Number out of range'

# Test the function with some example numbers
numbers = [525]
for number in numbers:
    print(number, ":", number_to_words(number))
