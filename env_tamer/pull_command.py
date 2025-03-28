from env_tamer_db.env_tamer_db import EnvTamerDb
from env_tamer.file_handler import FileHandler

def pull_command(directory, path):
    try:
        db = EnvTamerDb()
        env_vars = db.get_env_values(directory)
        env_vars_dict = {env_var.key : env_var.value for env_var in env_vars}
        fh = FileHandler(directory)
        fh.write_env_file(path, env_vars_dict)
        print(f'✅ Pull successful: {directory}, {path}')
    except Exception as ex:
        print(f'🛑 pull encountered an exception: {ex}')