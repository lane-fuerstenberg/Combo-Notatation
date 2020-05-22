from input import Input
import re


def convert(args):
    parsed_combo = []

    if isinstance(args, tuple):

        for arg in args:
            parsed_combo.append(replace_all_inputs_in(arg))
            pass

    else:

        parsed_combo.append(replace_all_inputs_in(args))

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
    diagonal = re.match("[UDBFudbf][UDBFudbf]", word) # this regex needs more tweaking inputs like ff will get ignored

    if diagonal:
        for key, value in Input.items():
            while does_key_has_match(key, diagonal.string):
                result = value

                for k in key:
                    word.replace(k, "", 1)
                    parsed_word += result
                    result = ""

                break

        return parsed_word

    for letter in word:
        for key, value in Input.items():
            while does_key_has_match(key, letter):
                result = value

                for k in key:
                    word = word.replace(k, "", 1)
                    parsed_word += result
                    result = ""

                break

    return parsed_word


def get_matching_key(keys, word):
    for key in keys:
        if key in word:
            return Input.get(keys)

    return ""

def does_key_has_match(keys, word):
    for key in keys:
        if key == word:
            return True

    return False