import tomlkit, os

config_path = os.path.abspath(__file__).replace('__init__.py','')

def config(key:str):
    with open(os.path.join(config_path,'config.toml')) as f:
        _config = tomlkit.parse(f.read())
    return _config[key]