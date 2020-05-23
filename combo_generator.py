from input import Input
import re


def convert(args):
    combo_list = []
    for arg in args:
        combo_list.append(replace_matching_key(arg))

    return combo_list


def replace_matching_key(word):
    regex_string = generate_regex_string()

    for keys, value in Input.items():
        for key in keys:
            regex = re.compile(regex_string[0] + key.replace("+", "\+") + regex_string[1])
            search = regex.search(word)
            if search:
                index = word.find(key, search.start())
                start = word[:index]
                end = word[index + len(key):]
                word = start + value + end

    return word


def get_matching_key(keys, word):
    for key in keys:
        if key in word:
            return Input.get(keys)

    return ""


def generate_regex_string():
    any_char_regex = r"[A-Z,a-z,0-9,+]*"
    starting_regex_string = r"(\A|<^|>)" + any_char_regex
    ending_regex_string = any_char_regex + r"(\Z|>^|<)"
    return starting_regex_string, ending_regex_string
