from .parameter import Parameter
from tlp import DATA_PATH
import re


class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_parameters(self, parameters_names):
        configs = self._get_parameters_from_config()
        return {name: self._get_param_value(text) 
                for name, text in configs.items()} 
     

    def _get_parameters_from_config(self):
        regex = re.compile('^([A-Z]|_|[0-9]|#)*=.*')
        with open(self.file_path) as config_file:
            self.text = config_file.read()
            get_name = lambda text: text.split('=')[0].replace('#', '')
            return {get_name(row): row 
                    for row in self.text.splitlines() 
                    if regex.match(row)}

    def _get_param_value(self, text):
        value = text.split('=')[1]
        return {'active' : not text.startswith('#'), 'value' : value}

    def save_as(self, parameters, file_path):
        self.file_path = file_path
        self.save(parameters)

    def save(self, parameters):
        with open(self.file_path, 'w') as config_file:
            text = reduce(lambda text, param: param.write(text),
                          [param for param in parameters if param.is_changed()],
                          self.text)
            config_file.write(text)

        self.load()
