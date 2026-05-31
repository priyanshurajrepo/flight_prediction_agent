from geopy.distance import geodesic

from airport_agent import get_airport_info

def get_distance(
    origin,
    destination
):

    origin_airport = get_airport_info(
        origin
    )

    destination_airport = get_airport_info(
        destination
    )

    coord1 = (
        origin_airport["lat"],
        origin_airport["lon"]
    )

    coord2 = (
        destination_airport["lat"],
        destination_airport["lon"]
    )

    return round(
        geodesic(
            coord1,
            coord2
        ).km,
        2
    )