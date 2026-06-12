from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from graph import graph
from risk_agent import get_risk_level

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Flight Risk API Running"
    }


@app.post("/predict")
def predict(data: dict):

    flight_number = data.get("flight_number")
    flight_date = data.get("flight_date")

    print("======== API DEBUG ========")
    print("Flight Number:", flight_number)
    print("Flight Date:", flight_date)
    print("===========================")

    result = graph.invoke(
        {
            "flight_number": flight_number,
            "flight_date": flight_date
        }
    )

    risk_score = result.get("risk_score", 0)
    risk_level = get_risk_level(risk_score)

    return {
        "flight": result.get("flight_number"),
        "airline": result.get("airline"),

        "origin": result.get("origin"),
        "destination": result.get("destination"),

        "flightStatus": result.get("flight_status"),

        "originAirport": result.get("origin_airport"),
        "destinationAirport": result.get("destination_airport"),

        "departureTime": result.get("departure_time"),

        "travelDate": result.get("travel_date"),

        "riskScore": risk_score,
        "riskLevel": risk_level,

        "riskBreakdown": result.get("risk_breakdown", {}),


        "weather": result.get("weather", {}),

        "delay": {
            "onTime": result.get("delay", {}).get("on_time", 0),
            "delayedFlights": result.get("delay", {}).get("delayed_flights", 0),
            "departures": result.get("delay", {}).get("departures", 0),
        },

        "history": {
            "cancelRate": result.get("history", {}).get("cancel_rate", 0),
            "technical": result.get("history", {}).get("technical", 0),
            "commercial": result.get("history", {}).get("commercial", 0),
            "operational": result.get("history", {}).get("operational", 0),
            "weather": result.get("history", {}).get("weather", 0),
            "misc": result.get("history", {}).get("misc", 0),
        },

        "analysis": result.get("explanation", "")
    }