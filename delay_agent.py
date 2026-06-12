import pandas as pd
from airline_mapper import AIRLINE_NORMALIZATION

df = pd.read_csv("data/delay.csv")


def get_delay_history(airline):

    airline = AIRLINE_NORMALIZATION.get(
    airline,
    airline
)

    airline_data = df[
    df["Airline"]
    .str.replace(" ", "")
    .str.lower()

    ==

    airline
    .replace(" ", "")
    .lower()
]
    

    if len(airline_data) == 0:

        print(f"No delay history found for {airline}")

        return {
          "on_time": 0,
          "delayed_flights": 0,
          "departures": 0
        }

    latest = airline_data.iloc[-1]

    return {

        "on_time":
        float(latest["% On-time Performance"]),

        "delayed_flights":
        int(latest["Number of flights Delayed"]),

        "departures":
        int(latest["Number of Departures"])

    }