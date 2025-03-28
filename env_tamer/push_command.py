from env_tamer_db.env_tamer_db import EnvTamerDb
from env_tamer.file_handler import FileHandler

def push_command(directory, file_name):
    try:
        fh = FileHandler(directory)
        env_vars_dict = fh.read_env_file(file_name)
        db = EnvTamerDb()
        db.save_env_values(directory, env_vars_dict)
        print(f'✅ Push successful: {directory}, {file_name}')
    except Exception as ex:
        print(f'🛑 push encountered an exception: {ex}')