import os 


class Config:
    BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': DevConfig,
}
