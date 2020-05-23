from input import Input
from stances import Stances
import re


def convert(args):
    combo_list = []
    for arg in args:
        combo_list.append(replace_matching_keys_in_word(arg))

    converted_combo = " ".join(str(x) for x in combo_list)

    for key, value in Stances.items():
        converted_combo = converted_combo.replace(value, key)

    return converted_combo


def replace_matching_keys_in_word(word):
    # regex for avoiding reading emote data as key
    regex_string = generate_regex_string()

    for keys, value in Input.items():
        for key in keys:
            # replaces + for \+ because it needs + to be read as literal
            regex = re.compile(regex_string[0] + key.replace("+", "\+") + regex_string[1])
            search = regex.search(word)

            while search:
                index = word.find(key, search.start())

                start = word[:index]
                end = word[index + len(key):]
                word = start + value + end

                # repeats search to find if multiples exist
                search = regex.search(word)

    return word


def generate_regex_string():
    # purpose of this method is to generate regex that will not read discord emote data as a key
    any_char_regex = r"[A-Z,a-z,0-9,+, ]*"
    starting_regex_string = r"(\A|<^|>)" + any_char_regex
    ending_regex_string = any_char_regex + r"(\Z|>^|<)"
    return starting_regex_string, ending_regex_string


def remove(word):
    m_start = re.search('^.+^<(?=<)', word)
    while m_start:
        word = word[m_start.end():]
        m_start = re.search('^.+^>(?=<)', word)

    m_end = re.search('(?<=>)^<.+$', word)
    while m_end:
        word = word[:m_end.start()]
        m_end = re.search('(?<=>)^<.+$', word)

    # cannot handle multiple removes still
    m_middle = re.search(r'(?<=>).+(?=<)', word)
    while m_middle:
        word = word[:m_middle.start()] + word[m_middle.end():]
        m_middle = re.search(r'(?<=>).+(?=<)', word)


    return word
