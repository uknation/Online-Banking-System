import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environ
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # this reads local .env
