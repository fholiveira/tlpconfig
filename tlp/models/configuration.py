from .parameter import Parameter
from functools import reduce
import re


class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
        self.refresh()
    
    def refresh(self):
        regex = re.compile('^([A-Z]|_|[0-9]|#)*=.*')
        with open(self.file_path) as config_file:
            self.text = config_file.read()

            self.parameters = [Parameter(row) 
                               for row in self.text.splitlines()
                               if regex.match(row)]

    def save_as(self, file_path):
        self.file_path = file_path
        self.save()

    def save(self):
        reduce(lambda text, param: param.write(text),
               [param for param in self.parameters if param.is_changed()],
               initializer=self.text)

        with open(file_path, 'w') as config_file:
            config_file.write(self.text)
