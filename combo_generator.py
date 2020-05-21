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
        parsed_combo += replace_matching_key(w)

    return parsed_combo


def replace_matching_key(word):
    parsed_word = ""
    for keys in Input.keys():
        result = get_matching_key(keys, word)
        if result:
            for values in Input.get(keys):
                word = word.replace(values, "")
            parsed_word += result[0]
            result = ""

    return parsed_word


def get_matching_key(keys, word):
    for key in keys:
        p = re.compile(f'{key}')
        if p.match(word):
            return Input.get(keys)

    return ""
