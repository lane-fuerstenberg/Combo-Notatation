from input import Input
import re


def convert(args):
    parsed_combo = []
    for arg in args:
        parsed_combo.append(replace_all_inputs_in(arg))
        pass

    return parsed_combo


def replace_all_inputs_in(word):
    for keys in Input.keys():

        # looks pretty bad but python automatically converts 1 length tuples into strings
        # this messes up the code if it does not validate that it has a tuple first (might be a better solution)
        if type(keys) is str:
            word = replace_with_string(keys, word)
        else:
            word = replace_with_tuple(keys, word)

    return word


def replace_with_string(keys, word):
    if re.search(r'\b{0}'.format(keys), word):
        word = word.replace(keys, Input.get(keys))
    return word


def replace_with_tuple(keys, word):
    for key in keys:
        if re.search(r'\b{0}'.format(key), word):
            word = word.replace(key, Input.get(keys))

    return word
