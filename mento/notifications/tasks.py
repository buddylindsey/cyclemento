from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import arrow

from mento.celery import app

from gear.models import Gear


@app.task
def check_for_needed_maintenance(user_id):
    user = User.objects.get(id=user_id)
    gears = Gear.objects.filter(user_id=user_id)

    for gear in gears:
        if gear.distance_since_last_maintenance() >= 1000.0:
            body = "Time for you to get a tune up on your {bike}.".format(
                gear.name)
            subject = "[CycleMento] Maintenance needed for {}".format(
                gear.name)
            email = EmailMessage(
                subject,body, 'no-reply@cyclemento.com', [user.email])
            email.send()
