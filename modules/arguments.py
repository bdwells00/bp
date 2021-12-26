
import argparse
from pathlib import Path
import sys
from betterprint.betterprint import bp
from betterprint.colortext import Ct
import betterprint.version as ver


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def file_check(f_to_c):
    """Check log file or error log file if it exists and if it should be
    appended.

    Args:
        - f_to_c (string): the file to check
    """
    file_to_check = Path(f_to_c)
    if file_to_check.is_file():
        check_append = input(f'{Ct.yellow}({f_to_c}) exists. Append? [Y/N]: {Ct.a}')
        # abort on no
        if check_append.lower() == 'n':
            bp(['Exiting', Ct.yellow], fil=0, err=1)
            sys.exit(1)
        # call file_check again if anything other than y (since n checked)
        elif check_append.lower() != 'y':
            bp([f'{check_append} is not "Y" or "N".', Ct.yellow], err=1, fil=0)
            file_check(f_to_c)
    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_args():
    """Get CLI arguments from argparse.

    Returns:
        - class 'argparse.ArgumentParser': Command Line Arguments
    """
    # Use argparse to capture cli parameters
    parser = argparse.ArgumentParser(
        prog=ver.__prog__,
        description=f'{Ct.bblue}{ver.ver}: {ver.__purpose__}{Ct.a}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='This program has no warranty. Please use with caution.',
        add_help=True)
    parser.add_argument('--date-log',
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
    parser.add_argument('--quiet',
                        help='quiet mode surpresses most output including '
                             'errors but keeps final summary',
                        action='store_true')
    parser.add_argument('-v',
                        '--verbose',
                        help='3 lvl incremental verbosity (-v, -vv, or -vvv)',
                        action='count',
                        default=0)
    parser.add_argument('--version',
                        help='print program version and exit',
                        action='version',
                        version=f'{Ct.bblue}{ver.ver}{Ct.a}')

    args = parser.parse_args()

    bp(['Checking if log_file exists and ask if it should be appended.',
        Ct.bmagenta], fil=0, veb=2)
    if args.log_file:
        file_check(args.log_file)
    bp(['Checking error_log_file exists and ask if it should be appended.',
        Ct.bmagenta], fil=0, veb=2)
    if args.error_log_file:
        file_check(args.error_log_file)
    if args.verbose > 3:
        bp([f'Verbosity level {args.verbose} requested. Using the maximum of 3.',
            Ct.yellow], err=1)

    return args
