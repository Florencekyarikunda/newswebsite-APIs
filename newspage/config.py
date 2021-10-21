import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = "56082198622f4891923b76a2fda0c2e8"
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # @staticmethod
    # def init_app(newspage):
    #         pass


# class ProdConfig(Config):
#     pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}