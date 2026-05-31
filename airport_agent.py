import pandas as pd

airports = pd.read_csv(
    "data/airports.csv"
)

def get_airport_info(iata_code):

    airport = airports[
        airports["iata_code"] == iata_code
    ]

    if airport.empty:
        return None

    airport = airport.iloc[0]

    return {

        "airport_name":
        airport["name"],

        "city":
        airport["municipality"],

        "lat":
        float(airport["latitude_deg"]),

        "lon":
        float(airport["longitude_deg"])

    }