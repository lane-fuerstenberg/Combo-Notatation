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

    diagonal = re.match(r"([UDFBudfb])[/]?(?!\1)[UDFBudfb]", word)
    multiple_press = re.match(r"[1-4]\+[1-4]\+?[1-4]?\+?[1-4]?", word)

    if diagonal or multiple_press:

        if diagonal:

            temp = diagonal

        else:

            temp = multiple_press

        for key, value in Input.items():

            if does_key_has_match(key, temp.string):

                result = value

                for k in key:

                    word.replace(k, "", 1)
                    parsed_word += result
                    result = ""

        return parsed_word

    for letter in word:

        for key, value in Input.items():

            if does_key_has_match(key, letter):
                result = value

                for k in key:

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
        if key == word:
            return True

    return False