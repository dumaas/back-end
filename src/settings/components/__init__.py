from pathlib import PurePath

from decouple import AutoConfig

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig()

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(__file__))
BASE_DIR = PurePath(__file__).parent.parent.parent

ENVIRONMENT = config("ENVIRONMENT", default="local")
