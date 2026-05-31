from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END

from weather_agent import get_weather

from explanation_agent import explain

from flight_lookup_agent import get_flight_details

from airport_agent import get_airport_info

from utils import convert_time
from distance_agent import get_distance

from airline_history_agent import get_cancellation_history

from delay_agent import get_delay_history

from risk_agent import calculate_risk


class FlightState(TypedDict):

    flight_number: str

    airline: str

    origin: str

    destination: str

    departure_time: str

    weather: dict

    explanation: str

    history: dict  

    delay: dict 

    risk_score: float


def weather_node(state):

    airport = get_airport_info(
        state["origin"]
    )

    weather = get_weather(
        airport["lat"],
        airport["lon"]
    )

    state["weather"] = weather

    return state



def risk_node(state):

    risk = calculate_risk(

    50,   # default ML score

    state["history"],

    state["delay"],

    state["weather"]

    )

    state["risk_score"] = risk

    return state


def explanation_node(state):

    state["explanation"] = explain(
    state["weather"],
    state["history"],
    state["delay"],
    state["risk_score"]
)

    print("\n===== EXPLANATION =====")
    print(state["explanation"])

    return state


def lookup_flight_node(state):

    flight = get_flight_details(
        state["flight_number"]
    )

    print("AIRLINE:", flight["airline"])

    if flight is None:

        raise ValueError(
            f"Flight {state['flight_number']} not found"
        )

    state["airline"] = flight["airline"]

    state["origin"] = flight["origin"]

    state["destination"] = flight["destination"]

    state["departure_time"] = flight["departure_time"]

    return state


def history_node(state):

    history = get_cancellation_history(
        state["airline"]
    )

    print("\n===== HISTORY =====")
    print(history)

    state["history"] = history

    return state


def delay_node(state):

    delay = get_delay_history(
        state["airline"]
    )

    state["delay"] = delay

    return state

builder = StateGraph(
    FlightState
)

builder.add_node(
    "weather",
    weather_node
)

builder.add_node(
    "history",
    history_node
)

builder.add_node(
    "delay",
    delay_node
)


builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "explanation",
    explanation_node
)

builder.add_node(
    "lookup",
    lookup_flight_node
)

builder.set_entry_point(
    "lookup"
)

builder.add_edge(
    "lookup",
    "weather"
)

builder.add_edge(
    "weather",
    "history"
)

builder.add_edge(
    "history",
    "delay"
)

builder.add_edge(
    "delay",
    "risk"
)

builder.add_edge(
    "risk",
    "explanation"
)

builder.add_edge(
    "explanation",
    END
)

graph = builder.compile()