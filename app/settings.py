import yaml


def load_settings(settings_source='./config/app.yaml'):
    with open(settings_source) as settings:
        return yaml.dump(yaml.load(settings))
