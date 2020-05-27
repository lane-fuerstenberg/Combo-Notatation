
# todo: needs all stances added to stances_raw

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
    'SWS'
)

Stances = {}

for stance in stances_raw:
    Stances[stance] = f"<{stance}>"

