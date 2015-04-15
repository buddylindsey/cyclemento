from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import arrow

from mento.celery import app

from accounts.utils import get_strava_client


@app.task
def get_gear(user_id):
    user = User.objects.get(id=user_id)
    client = get_strava_client(user)

    gear_ids = Activity.objects.filter(
        user=user).values_list('gear', flat=True)
