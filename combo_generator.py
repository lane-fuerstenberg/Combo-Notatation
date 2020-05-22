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
        while does_key_has_match(keys, word):
            result = Input.get(keys)
            if result:
                for k in keys:
                    word = word.replace(k, "", 1)
                parsed_word += result
                result = ""

    return parsed_word


def get_matching_key(keys, word):
    for key in keys:
        if key in word:
            return Input.get(keys)

    return ""

def does_key_has_match(keys, word):
    for key in keys:
        if key in word:
            return True

    return False
