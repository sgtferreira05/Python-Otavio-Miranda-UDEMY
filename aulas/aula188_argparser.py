# argparse.ArgumentParser to more complex command line arguments
# Official documentation: https://docs.python.org/3/library/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-name', '--name',
    # type=str, # type=int, # Type of the argument
    help='Name of the user.',
    metavar='STRING',
    required=False,
    # default='World', # Default value if no argument is passed
    # nargs='+', #Requires at least one argument
    action= 'append', # Appends the argument to a list
    )


parser.add_argument(
    '-v', '--verbose',
    help='Verbose mode.',
    action='store_true', # If the argument is passed, it will be True
    default=False, # Default value if no argument is passed
    )

args = parser.parse_args()

if args.name is None:
    print('No name was passed.')
else:
    print(f'Hello, {args.name}!')

print(f'Verbose mode: {args.verbose}')
# This script uses argparse to handle command line arguments.

# To run the script, use the command line and type:
# python aula188_argparser.py -name Ailton Ferreira

