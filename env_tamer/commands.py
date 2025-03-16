from env_tamer.env_tamer_db import EnvTamerDb
from env_tamer.file_handler import FileHandler


def init_command():
    db = EnvTamerDb()
    db.create_env_database()
    print(f'✅ init successful')

def push_command(directory, path):
    fh = FileHandler(directory)
    env_vars_dict = fh.read_env_file(path)
    db = EnvTamerDb()
    db.save_env_values(directory, env_vars_dict)
    print(f'✅ Push successful: {directory}, {path}')

def pull_command(directory, path):
    db = EnvTamerDb()
    env_vars = db.get_env_values(directory)
    env_vars_dict = {env_var.key : env_var.value for env_var in env_vars}
    fh = FileHandler(directory)
    fh.write_env_file(path, env_vars_dict)
    print(f'✅ Pull successful: {directory}, {path}')

def list_command(directory):
    db = EnvTamerDb()
    env_vars = db.get_env_values(directory)
    if len(env_vars) == 0:
        print(f'🛑 No Environment variables found for directory: {directory}')
    for env_var in env_vars:
        print(env_var)