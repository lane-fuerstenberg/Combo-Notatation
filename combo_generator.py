from input import Input

def convert(args):
    parsed_combo = []
    for arg in args:
        parsed_combo.append(replace_all_inputs_in(arg))
        pass

    return parsed_combo


def replace_all_inputs_in(string):
    updated_string = string.replace('uf', Input.WHITE_UF.value)
    return updated_string
