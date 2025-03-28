from env_tamer_db.env_tamer_db import EnvTamerDb

def init_command():
    try:
        db = EnvTamerDb()
        db.create_env_database()
        print(f'✅ init successful')
    except Exception as ex:
        print(f'🛑 init encountered an exception: {ex}')