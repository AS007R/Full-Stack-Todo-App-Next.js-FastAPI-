from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

BD_URL = config("BD_URL", cast=Secret)
TEST_BD_URL = config("TEST_BD_URL", cast=Secret)