from math import radians, cos, sin, asin, sqrt


def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """ Given two coordinates in decimal degrees, calculate the great circle distance
    in kilometers.
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # radius of earth in kilometers.
    return c * r


if __name__ == "__main__":
    # haversine function test
    print(haversine(13.5119498, 52.3648038, 10.899489, 49.900759))
