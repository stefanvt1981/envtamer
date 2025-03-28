import os
import re

class DirectoryNameSanitizer:
    def __init__(self, directory):
        self.directory = directory
        self.invalid_characters = re.compile(r'[<>:"/\\|?*]')
        self.reserved_names = {
            'CON', 'PRN', 'AUX', 'NUL',
            'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
            'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
        }

    def sanitize(self) -> str:
        for root, dirs, files in os.walk(self.directory, topdown=False):
            for name in dirs:
                sanitized_name = self.invalid_characters.sub('_', name)
                if sanitized_name.upper() in self.reserved_names:
                    sanitized_name = f'_{sanitized_name}'
                if sanitized_name != name:
                    os.rename(os.path.join(root, name), os.path.join(root, sanitized_name))
        return sanitized_name