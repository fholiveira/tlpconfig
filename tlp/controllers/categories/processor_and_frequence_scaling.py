from tlp.models import Group, NumericParameter, TextParameter, BooleanParameter


class ProcessorAndFrequenceScalingController:

    def __init__(self):
        self.groups= [Group('CPU_SCALING_GOVERNOR', 
                            [TextParameter('CPU_SCALING_GOVERNOR_ON_AC'),
                             TextParameter('CPU_SCALING_GOVERNOR_ON_BAT')]),
                      Group('CPU_SCALING_FREQ', 
                            [NumericParameter('CPU_SCALING_MIN_FREQ_ON_AC', reboot_needed=True), 
                             NumericParameter('CPU_SCALING_MAX_FREQ_ON_AC', reboot_needed=True), 
                             NumericParameter('CPU_SCALING_MIN_FREQ_ON_BAT', reboot_needed=True), 
                             NumericParameter('CPU_SCALING_MAX_FREQ_ON_BAT', reboot_needed=True)]),
                      Group('CPU_BOOST', 
                            [BooleanParameter('CPU_BOOST_ON_AC'), 
                             BooleanParameter('CPU_BOOST_ON_BAT')]),
                      Group('SCHED_POWERSAVE', 
                            [BooleanParameter('SCHED_POWERSAVE_ON_AC'), 
                             BooleanParameter('SCHED_POWERSAVE_ON_BAT')])]
