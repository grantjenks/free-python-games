import argparse
import os
import runpy

directory = os.path.dirname(os.path.realpath(__file__))
contents = os.listdir(directory)

def game_file(name):
    "Return True if filename represents a game."
    return not name.startswith('__') and name.endswith('.py')

games = sorted(name[:-3] for name in contents if game_file(name))

parser = argparse.ArgumentParser(
    prog='freegames',
    description='Free Python Games',
    epilog='Copyright 2017 Grant Jenks',
)
subparsers = parser.add_subparsers(dest='command', help='sub-command help')

parser_list = subparsers.add_parser('list', help='list games')

parser_copy = subparsers.add_parser('copy', help='copy game source code')
parser_copy.add_argument('game', choices=games, help='game name')
parser_copy.add_argument(
    '--force',
    action='store_true',
    help='overwrite existing file',
)

parser_show = subparsers.add_parser('show', help='show game source code')
parser_show.add_argument('game', choices=games, help='game name')

args = parser.parse_args()

if args.command == 'list':
    for game in games:
        print(game)
elif args.command == 'copy':
    filename = args.game + '.py'

    with open(os.path.join(directory, filename)) as reader:
        text = reader.read()

    cwd = os.getcwd()
    path = os.path.join(cwd, filename)

    if args.force or not os.path.exists(path):
        with open(path, 'w') as writer:
            writer.write(text)
    else:
        print('ERROR: File already exists. Specify --force to overwrite.')
else:
    assert args.command == 'show'
    
    with open(os.path.join(directory, args.game + '.py')) as reader:
        print(reader.read())
