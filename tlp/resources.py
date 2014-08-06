from pkg_resources import resource_filename


try:
    DATA_PATH = resource_filename('tlpconfig', 'data/')
except Exception:
    DATA_PATH = 'data/'


UI_PATH = DATA_PATH + 'ui/'
