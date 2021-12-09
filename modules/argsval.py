
import os
import sys
from betterprint.betterprint import bp
from betterprint.colortext import Ct
import modules.options as options


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def validate_args():
    """Validate the cli args before executing main()."""
    def file_check(f_to_c):
        """Check log file or error log file if it exists and if it should be
        appended.

        Args:
            - f_to_c (string): the file to check
        """
        bp([f'Starting validate_args()->file_check({f_to_c}).',
            Ct.BMAGENTA], fil=0, veb=3)
        if os.path.isfile(f_to_c):
            check_append = input(f'{Ct.YELLOW}({f_to_c}) exists. Append? '
                                 f'[Y/N]: {Ct.A}')
            # abort on no
            if check_append[:1].lower() == 'n':
                bp(['Exiting', Ct.YELLOW], fil=0, err=1)
                sys.exit(1)
            # call file_check again if anything other than y (since n checked)
            elif check_append[:1].lower() != 'y':
                bp([f'{check_append} is not "Y" or "N".', Ct.YELLOW], err=1,
                   fil=0)
                file_check(f_to_c)
    bp(['Checking if log_file exists and ask if it should be appended.',
        Ct.BMAGENTA], fil=0, veb=2)
    if options.args.log_file:
        file_check(options.args.log_file)
    bp(['Checking error_log_file exists and ask if it should be appended.',
        Ct.BMAGENTA], fil=0, veb=2)
    if options.args.error_log_file:
        file_check(options.args.error_log_file)
    if options.args.verbose > 3:
        bp([f'Verbosity level {options.args.verbose} requested. Using the'
            ' maximum of 3.', Ct.YELLOW], err=1)

    return
