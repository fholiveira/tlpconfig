from tlp.models import Group, TextParameter


class GraphicsCardsController:

    def __init__(self):
        self.groups= [Group('RADEON_POWER_PROFILE', 
                            [TextParameter('RADEON_POWER_PROFILE_ON_AC'),
                             TextParameter('RADEON_POWER_PROFILE_ON_BAT')]),
                      Group('RADEON_DPM_STATE', 
                            [TextParameter('RADEON_DPM_STATE_ON_AC'),
                             TextParameter('RADEON_DPM_STATE_ON_BAT')]),
                      Group('RADEON_DPM_PERF_LEVEL', 
                            [TextParameter('RADEON_DPM_PERF_LEVEL_ON_AC'),
                             TextParameter('RADEON_DPM_PERF_LEVEL_ON_BAT')])]
