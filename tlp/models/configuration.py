from .parameter import Parameter, Group
from functools import reduce
from itertools import chain
import json
import re


class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_groups();
        self.refresh()
    
    def load_groups(self):
        categories = None
        with open('data/categories.json') as config:
            categories = json.loads(config.read())

        load_parameters = lambda parameters: {parameter: None 
                                              for parameter in parameters}

        load_groups = lambda groups: [Group(group['name'],
                                            load_parameters(group['parameters']))
                             for group in groups]

        self.categories = {category['category']: load_groups(category['groups'])
                           for category in categories}

    def refresh(self):
        parameters = []
        regex = re.compile('^([A-Z]|_|[0-9]|#)*=.*')
        
        with open(self.file_path) as config_file:
            self.text = config_file.read()

            params = {parameter.name: parameter for parameter
                      in [Parameter.from_text(row)
                          for row in self.text.splitlines() 
                          if regex.match(row)]}
                          
        get = lambda name: params[name] if name in params else Parameter(name)
        groups = chain.from_iterable(groups for groups in self.categories.values())

        for group in groups:
            group.parameters = {name: get(name)
                                for name in group.parameters.keys()}

    def save_as(self, file_path):
        self.file_path = file_path
        self.save()

    def save(self):
        reduce(lambda text, param: param.write(text),
               [param for param in self.parameters if param.is_changed()],
               initializer=self.text)

        with open(file_path, 'w') as config_file:
            config_file.write(self.text)
