from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def explain(
    weather,
    history,
    delay,
    risk_score
):

    if risk_score < 25:
        risk_level = "LOW"

    elif risk_score < 50:
        risk_level = "MODERATE"

    else:
        risk_level = "HIGH"

    prompt = f"""
You are an aviation risk analyst.

Flight Risk Score:
{risk_score}/100

Final Risk Assessment:
{risk_level}

Current Weather:
Condition: {weather['condition']}
Visibility: {weather['visibility']} km
Temperature: {weather['temperature']}°C
Wind Speed: {weather['wind_speed']} km/h

Historical Cancellation Data:
Cancellation Rate: {history['cancel_rate']}%
Technical Cancellations: {history['technical']}
Operational Cancellations: {history['operational']}
Weather Cancellations: {history['weather']}

Historical Delay Data:
On-Time Performance: {delay['on_time']}%
Delayed Flights: {delay['delayed_flights']}
Total Departures: {delay['departures']}

IMPORTANT:
The final risk assessment has already been determined.

Use this exact risk assessment:
{risk_level}

Do NOT change it.
Do NOT recalculate it.
Do NOT classify the risk yourself.

Only explain the reasons behind this assessment.

Requirements:
- Mention on-time performance.
- Mention the main historical cancellation cause.
- Mention weather impact.
- Explain why the flight received the above assessment.
- Give a short passenger recommendation.
- Do not mention any raw ML probability.

Keep answer under 100 words.
"""

    response = llm.invoke(prompt)

    return response.content