#!/usr/bin/env python3


import random
import time
from betterprint.betterprint import bp, bp_dict
from betterprint.colortext import Ct
import modules.arguments as arguments
import modules.version as version


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def example_multi_bar(bar_count: int):
    """A multi-bar output example adapted from something found online. Used to
    demonstrate how to use bp to navigate multiple lines with overwrite.

    Args:
        bar_count (int): number of progress bars to display
    """
    bp([f'Create example_multi_bar using: {bar_count}:', Ct.bmagenta], veb=3)
    prog_counter = [0] * bar_count
    bp([f'Created prog_counter as: {prog_counter}', Ct.bmagenta],
       veb=3)
    bp(["\n" * bar_count, Ct.black], log=0, inl=1, num=0, fil=0)
    # if any bar is less than 100, continue
    while any(x < 100 for x in prog_counter):
        time.sleep(0.01)
        # pull out any progress that are under 100
        unfinished = [(i, v) for (i, v) in enumerate(prog_counter) if v < 100]
        # only care about index; this allows index to not be a tuple
        index, _ = random.choice(unfinished)
        # increment counter
        prog_counter[index] += 1
        # go all the way left 1000 spaces using 'D'
        bp(['\u001b[1000D', Ct.black], log=0, inl=1, num=0, fil=0)
        # go to the level of the index with 'A' going up
        bp([f'\u001b[{str(bar_count)}A', Ct.black], log=0, inl=1, num=0, fil=0)

        for progress in prog_counter:
            width = progress / 2
            bp(['[', Ct.a, '━' * int(width), Ct.black, '─' * (50 - int(width)),
               Ct.grey1, ']', Ct.a], inl=0, log=0, num=0, fil=0)
    bp(['Finished with example_multi_bar', Ct.bmagenta], veb=3)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def example_progress_bar(symbol='━', empty='─', symbol_color=Ct.a,
                         empty_color=Ct.grey1, bracket_color=Ct.a,
                         prog_width=50):
    """Show how to make a progress bar using bp.

    Args:
        - symbol (str, optional): the complete symbol. Defaults to '━'.
        - empty (str, optional): the empty symbol. Defaults to '─'.
        - symbol_color (str, optional): 'symbol' color. Defaults to Ct.A.
        - empty_color (str, optional): 'empty' color. Defaults to Ct.GREY1.
        - bracket_color (str, optional): 'bracket' color. Defaults to Ct.A.
        - prog_width (int, optional): progress bar width. Defaults to 50.
    """
    bp(['Entering example_progress_bar', Ct.bmagenta], veb=3)
    bp([f'Creating example_progress_bar using: {symbol} | {empty} | '
        f'{symbol_color} | {empty_color} | {bracket_color} | {prog_width}',
        Ct.bmagenta], veb=1, num=0)
    bp(['[', bracket_color, f'{empty * prog_width}', empty_color, ']',
        bracket_color], inl=1, fls=1, log=0, fil=0)
    bp(["\b" * (prog_width + 1), Ct.a], inl=1, log=0, fil=0)
    for _ in range(prog_width):
        time.sleep(0.05)
        bp([symbol, symbol_color], inl=1, fls=1, log=0, fil=0)
    bp(['', Ct.a], inl=0, log=0, fil=0)
    bp(['Finished with example_progress_bar.', Ct.bmagenta], veb=2)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def example_percent_complete(loops=50, loop_color=Ct.black, txt='Progress...'):
    """[summary]

    Args:
        - loops (int, optional): loops to completion. Defaults to 50.
        - loop_color (string, optional): color output. Defaults to Ct.BLACK.
        - txt (str, optional): text after percent. Defaults to 'Progress...'.
    """
    for idx, _ in enumerate(range(loops)):
        time.sleep(0.05)
        bp([f'\u001b[1000D{((idx + 1) / loops) * 100:.0f}% | {txt}',
            loop_color], inl=1, fls=1, log=0, num=0, fil=0)
    bp(['', Ct.a], log=0, fil=0)
    bp(['Finished with example_percent_complete.', Ct.bmagenta], veb=2)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def main():

    # ~~~ #             -examples-
    bp(['"This is error #420 with verbosity set to 1. This should show even'
        f' without verbosity at runtime (args.verbose={args.verbose}) '
        'because err overwrites veb', Ct.red], veb=1, err=2)
    """Call various examples using bp to show capabilities and ways to make it
    work for you."""
    bp(['Entering main().', Ct.bmagenta], veb=3)
    bp(['This text shows list position 0 with position 1 of default color,',
        Ct.a, ' and this text shows list position 2 with position 3 of Red.'
        ' This uses default settings.',
        Ct.red])
    bp(['Calling example_progress_bar(symbol="ꟷ", empty="ꟷ", symbol_color='
        'Ct.GREEN).', Ct.bmagenta], veb=2)
    example_progress_bar(symbol="ꟷ", empty="ꟷ", symbol_color=Ct.green)
    bp(['Returning from example_progress_bar(symbol="ꟷ", empty="ꟷ", '
        'symbol_color=Ct.GREEN).', Ct.bmagenta], veb=3)
    bp(['The next 3 print statements show verbosity levels 1-3 in order. Will'
        ' only be visible if that verbosity level requested', Ct.orange])
    bp(['Verbosity level 1', Ct.bmagenta], veb=1)
    bp(['Verbosity level 2', Ct.bmagenta], veb=2)
    bp(['Verbosity level 3', Ct.bmagenta], veb=3)
    bp(['Calling example_multi_bar(4).', Ct.bmagenta], veb=2)
    example_multi_bar(4)
    bp(['Returning from example_multi_bar(4).', Ct.bmagenta], veb=3)
    bp(['Calling example_progress_bar(symbol="═", empty="═", symbol_color'
        '=Ct.BROWN, prog_width=66) next', Ct.bmagenta], veb=2)
    example_progress_bar(symbol="═", empty="═", symbol_color=Ct.brown,
                         prog_width=66)
    bp(['Returning from  example_progress_bar(symbol="═", empty="═", '
        'symbol_color=Ct.BROWN, prog_width=66) next', Ct.bmagenta], veb=3)
    bp(['The next line is an empty line', Ct.a])
    bp(['', Ct.a])
    bp(['This shows numbers with default color: 19 00 ', Ct.a, 'and this with'
        ' text and numbers in green: 19 00 -67-', Ct.green], num=0)
    bp(['Calling example_progress_bar().', Ct.bmagenta], veb=2)
    example_progress_bar()
    bp(['Returning from example_progress_bar().', Ct.bmagenta], veb=3)
    bp(['The next 3 lines demonstrates error handling with the text within '
       'the "" the only part typed. The rest is added by "bp" using "err=2".',
        Ct.a])
    bp(['"This is error #423 with verbosity set to 1. This should show even'
        f' without verbosity at runtime (args.verbose={args.verbose}) '
        'because err overwrites veb', Ct.red], veb=1, err=2)
    bp(['"This is error #4244 with no number color"', Ct.red], num=0, err=2)
    bp(['"This is error 55, with default color"', Ct.a], err=2)
    bp(['Calling example_progress_bar(symbol="∞", empty="∞", symbol_color='
        'Ct.BLACK, prog_width=47) next', Ct.bmagenta], veb=2)
    example_progress_bar(symbol="∞", empty="∞", symbol_color=Ct.black,
                         prog_width=47)
    bp(['Returning from example_progress_bar(symbol="∞", empty="∞", '
        'symbol_color=Ct.BLACK, prog_width=47) next', Ct.bmagenta], veb=3)
    bp(['This is Warning #17171 in yellow using "err=1".', Ct.yellow], err=1)
    bp(['This is warning #15 with no number color', Ct.yellow], num=0, err=1)
    bp(['Calling example_percent_complete(loops=100).', Ct.bmagenta], veb=2)
    example_percent_complete(loops=100)
    bp(['Returning from example_percent_complete(loops=100).', Ct.bmagenta],
       veb=3)
    bp(['This next step will fail. It is commented out. Uncomment individually'
        ' to view the failures.', Ct.bmagenta], veb=1)
    # bp(['Raise exception with only 3 entries.', Ct.Z, 'This causes error'])
    # bp([example_percent_complete, Ct.bmagenta])
    bp(['Finished with "main()", in Yellow.', Ct.yellow], veb=2)


if __name__ == '__main__':

    # ~~~ #             -args-
    args = arguments.get_args()

    # ~~~ #             -title-
    bp([f'{version.ver} - {version.__purpose__}\n', Ct.bblue])

    # ~~~ #             -variables-
    bp_dict['color'] = 0 if args.no_color else 1
    bp_dict['date_log'] = 1 if args.date_log else 0
    bp_dict['log_file'] = args.log_file
    bp_dict['error_log_file'] = args.error_log_file
    bp_dict['quiet'] = 1 if args.quiet else 0
    bp_dict['verbose'] = args.verbose

    main()
