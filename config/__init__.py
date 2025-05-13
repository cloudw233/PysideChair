import tomlkit, os

config_path = os.path.abspath(__file__).replace('__init__.py','')

def init_config():
    if not os.path.exists(os.path.join(config_path,'config.toml')):
        with open(os.path.join(config_path,'config.toml'), 'w') as f,\
            open(os.path.join(config_path,'config.example.toml')) as r:
            f.write(r.read())

def config(key:str):
    with open(os.path.join(config_path,'config.toml')) as f:
        _config = tomlkit.parse(f.read())
    return _config[key]

def set_config(key:str, value):
    with open(os.path.join(config_path,'config.toml')) as f:
        _config = tomlkit.parse(f.read())
    _config[key] = value
    with open(os.path.join(config_path,'config.toml'), 'w') as f:
        f.write(tomlkit.dumps(_config))