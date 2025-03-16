import os

class FileHandler:
    def __init__(self, path):
        self.path = path

    def read_env_file(self, file_name):
        full_path = os.path.join(self.path, file_name)
        if os.path.exists(full_path):
            file = open(full_path)
            lines = file.read()
            envs = {}
            for line in lines:
                key, value = line.split('=')
                envs[key] = value
            return envs
        else:
            print(f'.env file path: {full_path} not found.')

    def write_env_file(self, file_name, envs):
        full_path = os.path.join(self.path, file_name)

        if os.path.exists(full_path):
            print(f'⚠️ An env file already exists at {full_path}')
            overwrite = input('Overwriting will delete the current file. Continue? (Y/N): ')

            if not overwrite == 'Y' or overwrite == 'y':
                print('🛑 Operation cancelled.')
                return

            with open(full_path, 'w') as file:
                for key, value in envs.items():
                    file.write(f'{key}={value}\n')

