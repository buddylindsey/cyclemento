import arrow

def ago(value):
    return arrow.get(value).humanize()
