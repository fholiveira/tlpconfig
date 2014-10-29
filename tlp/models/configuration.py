from functools import reduce
from . import Parameter
import re


class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_parameters(self, names):
        configs = self._get_parameters_from_config()
        return {name: self._get_param_status_and_value(text) 
                for name, text in configs.items()
                if name in names} 

    def _get_parameters_from_config(self):
        regex = re.compile('^([A-Z]|_|[0-9]|#)*=.*')
        with open(self.file_path) as config_file:
            self.text = config_file.read()
            get_name = lambda text: text.split('=')[0].replace('#', '')
            return {get_name(row): row 
                    for row in self.text.splitlines() 
                    if regex.match(row)}

    def _get_param_status_and_value(self, text):
        return (not text.startswith('#'), text.split('=')[1])

    def save_as(self, parameters, file_path):
        self.file_path = file_path
        self.save(parameters)

    def save(self, parameters):
        with open(self.file_path, 'w') as config_file:
            text = reduce(lambda text, param: self._write(text, param.to_text()),
                          [param for param in parameters],
                          self.text)
            config_file.write(text)
            self.text = text

    def _write(self, text, changes):
        old_parameter, new_parameter = changes
        if old_parameter in text:
            return text.replace(old_parameter, new_parameter)
        return text + '\n' + new_parameter 
