import os
from env_tamer.env_variable import Base, EnvVariable
from sqlalchemy import create_engine, MetaData, Engine, select
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session

class EnvTamerDb:

    def __init__(self):
        self.engine = None

        # get user home
        self.user_folder = os.path.expanduser('~')
        self.db_path = os.path.join(self.user_folder, ".envtamer")
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
        self.db_file = os.path.join(self.db_path, "envtamer.db")
        if os.name == 'nt':  # windows... duh
            self.db_file = self.db_file.replace("\\", "\\\\")

    def ensure_db(self):
        self.engine = create_engine(f"sqlite:///{self.db_file}")

    def create_env_database(self):
        try:
            if os.path.exists(self.db_file):
                print('🛑 Database file already exists. Initialization skipped.')
                self.engine = create_engine(f"sqlite:///{self.db_file}")
            else:
                engine = create_engine(f"sqlite:///{self.db_file}")
                if not database_exists(engine.url):
                    create_database(engine.url)
                    Base.metadata.create_all(engine)
                self.engine = engine
                print('️🗄️Empty database file created successfully.')
            print('🚀 Ready to push and pull env files.')
        except Exception as ex:
            print(f'🛑 Init went wrong: {ex}')

    def save_env_values(self, directory, variables):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                for (key, value) in variables:
                    stmt = select(EnvVariable).where(EnvVariable.directory == directory and EnvVariable.key == key)
                    existing_env = env_session.scalars(stmt).one()
                    if existing_env is None:
                        env_var = EnvVariable(
                            directory=directory,
                            key=key,
                            value=value
                        )
                        env_session.add(env_var)
                    else:
                        existing_env.value = value
                env_session.commit()
        except Exception as ex:
            print(f'🛑 save envs went wrong: {ex}')

    def save_env_value(self, directory, key, value):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                stmt = select(EnvVariable).where(EnvVariable.directory == directory and EnvVariable.key == key)
                existing_env = env_session.scalars(stmt).one()
                if existing_env is None:
                    env_var = EnvVariable(
                        directory=directory,
                        key=key,
                        value=value
                    )
                    env_session.add(env_var)
                else:
                    existing_env.value = value
                env_session.commit()
        except Exception as ex:
            print(f'🛑 save env went wrong: {ex}')

    def get_env_value(self, directory, key):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                stmt = select(EnvVariable).where(EnvVariable.directory == directory and EnvVariable.key == key)
                return env_session.scalars(stmt).one()
        except Exception as ex:
            print(f'🛑 get env went wrong: {ex}')

    def get_env_values(self, directory):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                stmt = select(EnvVariable).where(EnvVariable.directory == directory)
                return env_session.scalars(stmt).all()
        except Exception as ex:
            print(f'🛑 get all envs went wrong: {ex}')

    def delete_value(self, directory, key):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                stmt = select(EnvVariable).where(EnvVariable.directory == directory and EnvVariable.key == key)
                env_var = env_session.scalars(stmt).one()
                if env_var is not None:
                    env_session.delete(env_var)
                    env_session.commit()
        except Exception as ex:
            print(f'🛑 delete env went wrong: {ex}')

    def delete_values(self, directory):
        try:
            if self.engine is None:
                self.ensure_db()
            with Session(self.engine) as env_session:
                stmt = select(EnvVariable).where(EnvVariable.directory == directory)
                env_vars = env_session.scalars(stmt).all()
                for env_var in env_vars:
                    env_session.delete(env_var)
                env_session.commit()
        except Exception as ex:
            print(f'🛑 delete env went wrong: {ex}')