
__author__ = 'Brandon Wells <wellsb.prog@gmail.com>'
__license__ = 'MIT'
__origin_date__ = '2021-11-25'
__prog__ = 'bp.py'
__purpose__ = 'colorization module "Better Print" (bp)'
__version__ = '0.2.1'
__version_date__ = '2021-12-02'
__version_info__ = tuple(int(i) for i in __version__.split('.') if i.isdigit())


import argparse


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_args():
    """Get CLI arguments from argparse.

    Returns:
        - class 'argparse.ArgumentParser': Command Line Arguments
    """
    # Use argparse to capture cli parameters
    parser = argparse.ArgumentParser(
        prog=__prog__,
        description=f'{ver}: {__purpose__}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='This program has no warranty. Please use with caution.',
        add_help=True)
    parser.add_argument('--log',
                        help='add timestamp logging to output',
                        action='store_true')
    parser.add_argument('--log-file',
                        help='file to save output',
                        metavar='<filename>',
                        type=str)
    parser.add_argument('--error-log-file',
                        help='file to save output',
                        metavar='<filename>',
                        type=str)
    parser.add_argument('--no-color',
                        help='don\'t colorize output',
                        action='store_true')
    parser.add_argument('-v',
                        '--verbose',
                        help='3 lvl incremental verbosity (-v, -vv, or -vvv)',
                        action='count',
                        default=0)
    parser.add_argument('--version',
                        help='print program version and exit',
                        action='version',
                        version=f'{ver}')

    return parser.parse_args()


print_tracker = 0
ver = f'{__prog__} v{__version__} ({__version_date__})'
args = get_args()
