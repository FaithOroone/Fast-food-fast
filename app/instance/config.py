class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'postgresql://postgres:12345@kerenagemo@localhost:5432/fast_food_fast'


class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
