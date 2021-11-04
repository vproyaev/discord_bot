import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = env.str('CHANNEL_ID')
