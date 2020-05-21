from input import Input
import re


def convert(args):
    parsed_combo = []
    for arg in args:
        parsed_combo.append(replace_all_inputs_in(arg))
        pass

    return parsed_combo


def replace_all_inputs_in(word):
    first_digit = re.search(r"\d", word)
    words = (word[:first_digit.start()], word[first_digit.start():])
    parsed_combo = ""
    for w in words:
        print(w)
        parsed_combo += replace_matching_key(w)

    return parsed_combo


def replace_matching_key(word):
    parsed_word = ""
    for keys in Input.keys():

        # looks pretty bad but python automatically converts 1 length tuples into strings
        # this messes up the code if it does not validate that it has a tuple first (might be a better solution)
        if type(keys) is str:
            parsed_word += replace_with_string(keys, word)
        else:
            parsed_word += replace_with_tuple(keys, word)

    return parsed_word


def replace_with_string(key, word):
    if key in word:
        return Input.get(key)

    return ""


def replace_with_tuple(keys, word):
    for key in keys:
        if key in word:
            return Input.get(keys)

    return ""
