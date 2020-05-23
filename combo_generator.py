from input import Input
import re


def convert(args):
    combo_list = []
    for arg in args:
        combo_list.append(replace_matching_keys_in_word(arg))

    return combo_list


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


def get_matching_key(keys, word):
    for key in keys:
        if key in word:
            return Input.get(keys)

    return ""


def generate_regex_string():
    # purpose of this method is to generate regex that will not read discord emote data as a key
    any_char_regex = r"[A-Z,a-z,0-9,+]*"
    starting_regex_string = r"(\A|<^|>)" + any_char_regex
    ending_regex_string = any_char_regex + r"(\Z|>^|<)"
    return starting_regex_string, ending_regex_string
