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

Flight Risk Score: {risk_score}

Weather:
- Condition: {weather['condition']}
- Temperature: {weather['temperature']}
- Visibility: {weather['visibility']} km

Delay History:
- On-Time Performance: {delay['on_time']}%

Cancellation History:
- Cancellation Rate: {history['cancel_rate']}%

Generate output in EXACTLY this format:

Risk Summary

• Weather Impact: one short sentence

• Delay History: one short sentence

• Cancellation Trend: one short sentence

Recommendation:
one short recommendation

Keep response under 80 words.
"""

    response = llm.invoke(prompt)

    return response.content