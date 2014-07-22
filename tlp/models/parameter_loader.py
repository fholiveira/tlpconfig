from .parameter import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)

class ParameterLoader():
    def __init__(self):
        parameters = [NumericParameter('DISK_IDLE_SECS_ON_AC'),
                      NumericParameter('DISK_IDLE_SECS_ON_BAT'),
                      NumericParameter('MAX_LOST_WORK_SECS_ON_AC'),
                      NumericParameter('MAX_LOST_WORK_SECS_ON_BAT'),
                      TextParameter('CPU_SCALING_GOVERNOR_ON_AC'),
                      TextParameter('CPU_SCALING_GOVERNOR_ON_BAT'),
                      NumericParameter('CPU_SCALING_MIN_FREQ_ON_AC'),
                      NumericParameter('CPU_SCALING_MAX_FREQ_ON_AC'),
                      NumericParameter('CPU_SCALING_MIN_FREQ_ON_BAT'),
                      NumericParameter('CPU_SCALING_MAX_FREQ_ON_BAT'),
                      BooleanParameter('CPU_BOOST_ON_AC'),
                      BooleanParameter('CPU_BOOST_ON_BAT'),
                      BooleanParameter('SCHED_POWERSAVE_ON_AC'),
                      BooleanParameter('SCHED_POWERSAVE_ON_BAT'),
                      BooleanParameter('NMI_WATCHDOG'),
                      TextParameter('PHC_CONTROLS', quotes='"'),
                      TextParameter('PCIE_ASPM_ON_AC'),
                      TextParameter('PCIE_ASPM_ON_BAT'),
                      TextParameter('RADEON_POWER_PROFILE_ON_AC'),
                      TextParameter('RADEON_POWER_PROFILE_ON_BAT'),
                      TextParameter('RADEON_DPM_STATE_ON_AC'),
                      TextParameter('RADEON_DPM_STATE_ON_BAT'),
                      TextParameter('RADEON_DPM_PERF_LEVEL_ON_AC'),
                      TextParameter('RADEON_DPM_PERF_LEVEL_ON_BAT'),
                      BooleanParameter('WIFI_PWR_ON_AC', yes='5', no='1'),
                      BooleanParameter('WIFI_PWR_ON_BAT', yes='5', no='1'),
                      BooleanParameter('WOL_DISABLE', yes='Y', no='N'),
                      NumericParameter('SOUND_POWER_SAVE_ON_AC'),
                      NumericParameter('SOUND_POWER_SAVE_ON_BAT'),
                      TextParameter('SOUND_POWER_SAVE_CONTROLLER'),
                      BooleanParameter('RESTORE_DEVICE_STATE_ON_STARTUP'),
                      ListParameter('DEVICES_TO_DISABLE_ON_STARTUP'),
                      ListParameter('DEVICES_TO_ENABLE_ON_STARTUP'),
                      ListParameter('DEVICES_TO_DISABLE_ON_SHUTDOWN'),
                      ListParameter('DEVICES_TO_ENABLE_ON_SHUTDOWN'),
                      ListParameter('DEVICES_TO_ENABLE_ON_RADIOSW'),
                      NumericParameter('START_CHARGE_THRESH_BAT0'),
                      NumericParameter('STOP_CHARGE_THRESH_BAT0'),
                      NumericParameter('START_CHARGE_THRESH_BAT1'),
                      NumericParameter('STOP_CHARGE_THRESH_BAT1'),
                      BooleanParameter('DISABLE_TPACPIBAT')]

        self.parameters = {parameter.name: parameter
                           for parameter in parameters}

    def from_text(self, text):
        values = text.split('=')
        name = values[0].replace('#', '')
        initial_state = {'active' : not text.startswith('#'),
                         'value' : values[1].replace('"', '')}

        parameter = self.parameters.get(name)
        if parameter:
            parameter.initial_state = initial_state
            parameter.active = initial_state['active']
            parameter._value = initial_state['value']

        return parameter
