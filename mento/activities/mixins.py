class DistanceMixin(object):
    def calculate_distance(self, distance, unit='m'):
        units = {'m': 0.000621371, 'ft': 0.000189394, 'mi': 1, 'km': 0.621371}
        return round(distance * units.get(unit, 1), 1)
