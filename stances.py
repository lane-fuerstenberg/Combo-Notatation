
# todo: needs all stances added to stances_raw

# Used to represent stances in text format
# Essentially the code validates that all parts of the string read have < on left and > on right.
# This is how it validates that it has already replaced that string
# It will use stance dictionary to insert <> around stance then removes at the very end

# Possibly a bad solution? If you process this in order though you have an issue of needing to create insane regex
# just to prevent code from reading 1+2 as the 1. It needs to either read ahead or the first number or to search for
# 1+2 first by having a priority of order, which means that you are no longer reading the string in order.
# Just explaining reasoning behind an abstract solution.

# All stances are inserted into input dictionary in for loop, they need to be separate due to post processing removal
# see combo_generator line 17
stances_raw = (
    'DCK',
    'FLK',
    'SEN',
    'SNK',
    'DES',
    'RWV',
    'LWV',
    'DSS',
    'SWAY',
    'SWY',
    'RSS',
    'FLY',
    'SWS',
    'DFLIP',
    'FC',
    'WS'
)

Stances = {}

for stance in stances_raw:
    Stances[stance] = f"<{stance}>"

