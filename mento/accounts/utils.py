import random
import string

from stravalib.client import Client


def generate_password():
    return ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in xrange(9)])


def get_strava_client(user):
    strava = user.social_auth.get()
    return Client(access_token=strava.tokens)
