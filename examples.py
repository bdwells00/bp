import random
import time
from bp import Ct, bp
import global_args as ga


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def example_multi_bar(bar_count: int):
    """A multi-bar output example adapted from something found online. Used to
    demonstrate how to use bp to navigate multiple lines with overwrite.

    Args:
        bar_count (int): number of progress bars to display
    """
    bp([f'Create example_multi_bar using: {bar_count}:', Ct.BMAGENTA], veb=3)
    prog_counter = [0] * bar_count
    bp([f'Created prog_counter as: {prog_counter}', Ct.BMAGENTA],
       veb=3)
    bp(["\n" * bar_count, Ct.BLACK], log=0, inl=1, num=0, fil=0)
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
        bp(['\u001b[1000D', Ct.BLACK], log=0, inl=1, num=0, fil=0)
        # go to the level of the index with 'A' going up
        bp([f'\u001b[{str(bar_count)}A', Ct.BLACK], log=0, inl=1, num=0, fil=0)

        for progress in prog_counter:
            width = progress / 2
            bp(['[', Ct.A, '━' * int(width), Ct.BLACK, '─' * (50 -
               int(width)), Ct.GREY1, ']', Ct.A], inl=0, log=0, num=0, fil=0)
    bp(['Finished with example_multi_bar', Ct.BMAGENTA], veb=3)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def example_progress_bar(symbol='━', empty='─', symbol_color=Ct.A,
                         empty_color=Ct.GREY1, bracket_color=Ct.A,
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
    bp(['Entering example_progress_bar', Ct.BMAGENTA], veb=3)
    bp([f'Creating example_progress_bar using: {symbol} | {empty} | '
        f'{symbol_color} | {empty_color} | {bracket_color} | {prog_width}',
        Ct.BMAGENTA], veb=1, num=0)
    bp(['[', bracket_color, f'{empty * prog_width}', empty_color, ']',
        bracket_color], inl=1, fls=1, log=0, fil=0)
    bp(["\b" * (prog_width + 1), Ct.A], inl=1, log=0, fil=0)
    for i in range(prog_width):
        time.sleep(0.05)
        bp([symbol, symbol_color], inl=1, fls=1, log=0, fil=0)
    bp(['', Ct.A], inl=0, log=0, fil=0)
    bp(['Finished with example_progress_bar.', Ct.BMAGENTA], veb=2)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def example_percent_complete(loops=50, loop_color=Ct.BLACK, txt='Progress...'):
    """[summary]

    Args:
        - loops (int, optional): loops to completion. Defaults to 50.
        - loop_color (string, optional): color output. Defaults to Ct.BLACK.
        - txt (str, optional): text after percent. Defaults to 'Progress...'.
    """
    for_loop = 0
    for _ in range(loops):
        time.sleep(0.05)
        for_loop += 1
        bp([f'\u001b[1000D{(for_loop / loops) * 100:.0f}% | {txt}',
            loop_color], inl=1, fls=1, log=0, num=0, fil=0)
    bp(['', Ct.A], log=0, fil=0)
    bp(['Finished with example_percent_complete.', Ct.BMAGENTA], veb=2)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def examples():
    """Call various examples using bp to show capabilities and ways to make it
    work for you."""
    bp(['Entering examples().', Ct.BMAGENTA], veb=3)
    bp(['This text shows list position 0 with position 1 of default color,',
        Ct.A, ' and this text shows list position 2 with position 3 of Red.'
        ' This uses default settings.',
        Ct.RED])
    bp(['Calling example_progress_bar(symbol="ꟷ", empty="ꟷ", symbol_color='
        'Ct.GREEN).', Ct.BMAGENTA], veb=2)
    example_progress_bar(symbol="ꟷ", empty="ꟷ", symbol_color=Ct.GREEN)
    bp(['Returning from example_progress_bar(symbol="ꟷ", empty="ꟷ", '
        'symbol_color=Ct.GREEN).', Ct.BMAGENTA], veb=3)
    bp(['The next 3 print statements show verbosity levels 1-3 in order. Will'
        ' only be visible if that verbosity level requested', Ct.ORANGE])
    bp(['Verbosity level 1', Ct.BMAGENTA], veb=1)
    bp(['Verbosity level 2', Ct.BMAGENTA], veb=2)
    bp(['Verbosity level 3', Ct.BMAGENTA], veb=3)
    bp(['Calling example_multi_bar(4).', Ct.BMAGENTA], veb=2)
    example_multi_bar(4)
    bp(['Returning from example_multi_bar(4).', Ct.BMAGENTA], veb=3)
    bp(['Calling example_progress_bar(symbol="═", empty="═", symbol_color'
        '=Ct.BROWN, prog_width=66) next', Ct.BMAGENTA], veb=2)
    example_progress_bar(symbol="═", empty="═", symbol_color=Ct.BROWN,
                         prog_width=66)
    bp(['Returning from  example_progress_bar(symbol="═", empty="═", '
        'symbol_color=Ct.BROWN, prog_width=66) next', Ct.BMAGENTA], veb=3)
    bp(['The next line is an empty line', Ct.A])
    bp(['', Ct.A])
    bp(['This shows numbers with default color: 19 00 ', Ct.A, 'and this with'
        ' text and numbers in green: 19 00 -67-', Ct.GREEN], num=0)
    bp(['Calling example_progress_bar().', Ct.BMAGENTA], veb=2)
    example_progress_bar()
    bp(['Returning from example_progress_bar().', Ct.BMAGENTA], veb=3)
    bp(['The next 3 lines demonstrates error handling with the text within '
       'the "" the only part typed. The rest is added by "bp" using "erl=2".',
        Ct.A])
    bp(['"This is error #423 with verbosity set to 1. This should show even'
        f' without verbosity at runtime (args.verbose={ga.args.verbose}) '
        'because erl overwrites veb', Ct.RED], veb=1, erl=2)
    bp(['"This is error #4244 with no number color"', Ct.RED], num=0, erl=2)
    bp(['"This is error 55, with default color"', Ct.A], erl=2)
    bp(['Calling example_progress_bar(symbol="∞", empty="∞", symbol_color='
        'Ct.BLACK, prog_width=47) next', Ct.BMAGENTA], veb=2)
    example_progress_bar(symbol="∞", empty="∞", symbol_color=Ct.BLACK,
                         prog_width=47)
    bp(['Returning from example_progress_bar(symbol="∞", empty="∞", '
        'symbol_color=Ct.BLACK, prog_width=47) next', Ct.BMAGENTA], veb=3)
    bp(['This is Warning #17171 in yellow using "erl=1".', Ct.YELLOW], erl=1)
    bp(['This is warning #15 with no number color', Ct.YELLOW], num=0, erl=1)
    bp(['Calling example_percent_complete(loops=100).', Ct.BMAGENTA], veb=2)
    example_percent_complete(loops=100)
    bp(['Returning from example_percent_complete(loops=100).', Ct.BMAGENTA],
       veb=3)
    bp(['This next step will fail. It is commented out. Uncomment individually'
        ' to view the failures.', Ct.BMAGENTA], veb=1)
    # bp(['Raise exception with only 3 entries.', Ct.Z, 'This causes error'])
    # bp([example_percent_complete, Ct.BMAGENTA])
    bp(['Finished with "examples", in Yellow.', Ct.YELLOW], veb=2)


if __name__ == '__main__':

    examples()
