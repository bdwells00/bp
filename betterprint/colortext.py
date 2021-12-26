'''colortext.py v0.1.1'''

from dataclasses import dataclass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
@dataclass
class ColorText:
    """A class of constants used to color strings for console printing.
    """
    __slots__ = (
        'a',
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
        'bblack',
        'bred',
        'bgreen',
        'byellow',
        'bblue',
        'bmagenta',
        'bcyan',
        'bwhite',
        'grey1',
        'grey2',
        'grey3',
        'grey4',
        'grey5',
        'grey6',
        'grey7',
        'grey8',
        'grey9',
        'grey10',
        'grey11',
        'grey12',
        'orange',
        'brown',
    )


Ct = ColorText()
Ct.a = '\u001b[0m'
Ct.black = '\u001b[38;5;0m'
Ct.red = '\u001b[38;5;1m'
Ct.green = '\u001b[38;5;2m'
Ct.yellow = '\u001b[38;5;3m'
Ct.blue = '\u001b[38;5;4m'
Ct.magenta = '\u001b[38;5;5m'
Ct.cyan = '\u001b[38;5;6m'
Ct.white = '\u001b[38;5;7m'
Ct.bblack = '\u001b[38;5;8m'
Ct.bred = '\u001b[38;5;9m'
Ct.bgreen = '\u001b[38;5;10m'
Ct.byellow = '\u001b[38;5;11m'
Ct.bblue = '\u001b[38;5;12m'
Ct.bmagenta = '\u001b[38;5;13m'
Ct.bcyan = '\u001b[38;5;14m'
Ct.bwhite = '\u001b[38;5;15m'
Ct.grey1 = '\u001b[38;5;255m'
Ct.grey2 = '\u001b[38;5;253m'
Ct.grey3 = '\u001b[38;5;251m'
Ct.grey4 = '\u001b[38;5;249m'
Ct.grey5 = '\u001b[38;5;247m'
Ct.grey6 = '\u001b[38;5;245m'
Ct.grey7 = '\u001b[38;5;243m'
Ct.grey8 = '\u001b[38;5;241m'
Ct.grey9 = '\u001b[38;5;239m'
Ct.grey10 = '\u001b[38;5;237m'
Ct.grey12 = '\u001b[38;5;233m'
Ct.orange = '\u001b[38;2;233;133;33m'
Ct.brown = '\u001b[38;2;118;65;12m'
