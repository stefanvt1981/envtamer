import click
import os
from env_tamer.commands import init_command, push_command, pull_command, list_command

possible_commands = ['init', 'pull', 'push', 'list']

@click.command()
@click.argument('command')
@click.option('--directory', '-d',default=os.getcwd(), help='Name of the directory to push. Defaults to current working directory if not specified.')
@click.option('--path', '-p', default='.env', help='Path to the env file. Defaults to \'.env\' in the specified or current directory.')
def tame_env(command, directory, path):
    match command:
        case 'init':
            init_command()
        case 'push':
            push_command(directory, path)
        case 'pull':
            pull_command(directory, path),
        case 'list':
            list_command(directory),
        case _:
            print(f'Choose one of the following commands: {possible_commands}')

if __name__ == '__main__':
    tame_env()