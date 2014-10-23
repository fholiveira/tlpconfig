from tlp.models import Group, NumericParameter, TextParameter


class UndervoltingController:

    def __init__(self):
        self.groups= [Group('PHC', [TextParameter('PHC_CONTROLS', quotes='"')])]
