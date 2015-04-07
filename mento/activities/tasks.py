from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import arrow

from mento.celery import app

from accounts.utils import get_strava_client

from .models import Activity
from notifications.tasks import check_for_needed_maintenance


def log_email(task, message):
    email = EmailMessage(
        "[CycleMento] Task: {}".format(task), message,
        'no-reply@cyclemento.com', ['buddy@buddylindsey.com'])
    email.send()


@app.task
def get_strava_activities_by_user(user_id, days=None):
    user = User.objects.get(id=user_id)
    client = get_strava_client(user)

    if days:
        end = arrow.utcnow()
        start = end.replace(days=(0-days))

        activity_iter = client.get_activities(
            before=end.datetime, after=start.datetime)
    else:
         activity_iter = client.get_activities()

    acts = []

    for activity in activity_iter:
        act, created = Activity.objects.get_or_create(
            external_id=activity.id, source=Activity.SOURCES.strava,
            user=user)

        act.update_with_strava(activity)
        acts.append(act)

    check_for_needed_maintenance.delay(user_id)

    log_email('get_strava_activities_by_user',
              "Total {} added for user {}".format(len(acts), user.username))


@app.task
def retrieve_activities(days=None):
    users = User.objects.filter(
        social_auth__provider='strava').values_list('id', flat=True)

    for user in users:
        get_strava_activities_by_user.delay(user_id=user, days=1)
