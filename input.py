from emote import *
from stances import Stances

# todo: needs capital directions to be set to dark directional emotes

Input = {
    ('CD', 'cd'): F + N + D + DF,
    ('hcb', 'hcb+', 'HCB', 'HCB+'): F + DF + D + DB + B,
    ('hcf', 'hcf+', 'HCF', 'HCF+'): B + DB + D + DF + F,
    ('qcf', 'qcf+', 'QCF', 'QCF+'): D + DF + F,
    ('qcb', 'qcb+', 'QCB', 'QCB+'): D + DB + B,
    ('wr', 'wr+', 'WR', 'WR+'): F + F + F,
    ('uf', 'u/f', 'uf+', 'u/f+'): UF,
    ('df', 'd/f', 'df+', 'd/f+'): DF,
    ('db', 'd/b', 'db+', 'd/b+'): DB,
    ('ub', 'u/b', 'ub+', 'u/b+'): UB,
    ('d', 'd+'): D,
    ('b', 'b+'): B,
    ('u', 'u+'): U,
    ('f', 'f+'): F,
    ('1+2+3+4',): NUM1234,
    ('2+3+4',): NUM234,
    ('1+3+4',): NUM134,
    ('1+2+4',): NUM124,
    ('1+2+3',): NUM123,
    ('3+4',): NUM34,
    ('2+4',): NUM24,
    ('2+3',): NUM23,
    ('1+4',): NUM14,
    ('1+3',): NUM13,
    ('1+2',): NUM12,
    ('4',): NUM4,
    ('3',): NUM3,
    ('2',): NUM2,
    ('1',): NUM1,
    (',',): SPACER,
    ('N', 'n', 'N+', 'n+'): N
}


for key, value in Stances.items():
    Input.__setitem__((key.lower(), key.upper()), value)

