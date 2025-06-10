import os
import environ
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environ
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # this reads local .env
