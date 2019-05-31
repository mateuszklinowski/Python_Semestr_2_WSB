
import string

def shift(number):
    min = 97
    max = 123
    if number > max:
        return number- max + min
    elif number < min:
        return number + max - min
    return number

def cezar(word,move):
    word_list = list(word)
    mapped = list(map(lambda char: ord(char), word_list))
    moved = list(map(lambda char: char + move, mapped))
    shifted = list(map(shift,moved))
    back_to_char = list(map(lambda char: chr(char), shifted))
    return ''.join(back_to_char)

print(cezar('asd',2))
