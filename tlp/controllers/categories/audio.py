from tlp.models import Group, NumericParameter, TextParameter


class AudioController:

    def __init__(self):
        self.groups= [Group('SOUND_POWER_SAVE', 
                            [NumericParameter('SOUND_POWER_SAVE_ON_AC'),
                             NumericParameter('SOUND_POWER_SAVE_ON_BAT')]),
                      Group('SOUND_POWER_CONTROLLER', 
                            [TextParameter('SOUND_POWER_SAVE_CONTROLLER')])]
