import pandas as pd
from airline_mapper import AIRLINE_NORMALIZATION

df = pd.read_csv("data/cancellation.csv")


def get_cancellation_history(airline):

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

        print(f"No cancellation history found for {airline}")

        return {
            "cancel_rate": 0,
            "technical": 0,
            "commercial": 0,
            "operational": 0,
            "weather": 0,
            "misc": 0
        }

    latest = airline_data.iloc[-1]

    return {
        "cancel_rate": float(latest["% Cancellation"]),
        "technical": int(latest["Cancellation Due to Technical"]),
        "commercial": int(latest["Cancellation Due to Commercial"]),
        "operational": int(latest["Cancellation Due to Operational"]),
        "weather": int(latest["Cancellation Due to Weather"]),
        "misc": int(latest["Cancellation Due to Misc"])
    }