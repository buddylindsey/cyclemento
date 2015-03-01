from accounts.utils import get_strava_client


def get_strava_gear(activity, gear_id=None):
    from .models import Gear
    gear, created = Gear.objects.get_or_create(
        user=activity.user, external_id=gear_id)

    if created:
        client = get_strava_client(activity.user)
        strava_gear = client.get_gear(gear_id)

        gear.update_with_strava(strava_gear)

    return gear
