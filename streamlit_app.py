import streamlit as st
import pandas as pd

from graph import graph
from risk_agent import get_risk_level

st.set_page_config(
    page_title="Flight Risk Predictor",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Flight Risk Predictor")

flight_number = st.text_input(
    "Enter Flight Number",
    placeholder="e.g. AI302"
)

if st.button("Analyze Flight"):

    if not flight_number:
        st.warning("Please enter a flight number.")
        st.stop()

    with st.spinner("Analyzing flight..."):

        try:

            result = graph.invoke(
                {
                    "flight_number": flight_number
                }
            )

        except Exception as e:

            st.error(
                f"Flight not found or data unavailable.\n\n{e}"
            )

            st.stop()

    st.success("Analysis Complete")

    risk_level = get_risk_level(
        result["risk_score"]
    )

    # ==========================
    # Flight Details
    # ==========================

    st.subheader("✈️ Flight Details")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Flight",
            result["flight_number"]
        )

    with col2:
        st.metric(
            "Airline",
            result["airline"]
        )

    with col3:

        st.metric(
            "Risk Score",
            f"{result['risk_score']}/100"
        )

        st.progress(
            result["risk_score"] / 100
        )

        st.caption(
            f"{result['risk_score']} / 100"
        )

    with col4:

        st.write("### Risk Level")

        if risk_level == "LOW":
            st.success("🟢 LOW")

        elif risk_level == "MODERATE":
            st.warning("🟡 MODERATE")

        else:
            st.error("🔴 HIGH")

    st.divider()

    # ==========================
    # Route
    # ==========================

    st.subheader("🌍 Route")

    st.write(
        f"### {result['origin']} ➜ {result['destination']}"
    )

    st.divider()

    # ==========================
    # Weather
    # ==========================

    st.subheader("🌦 Weather")

    weather = result["weather"]

    w1, w2, w3, w4 = st.columns(4)

    with w1:
        st.metric(
            "🌡 Temperature",
            f"{weather['temperature']}°C"
        )

    with w2:
        st.metric(
            "👁 Visibility",
            f"{weather['visibility']} km"
        )

    with w3:
        st.metric(
            "💨 Wind Speed",
            f"{weather['wind_speed']} km/h"
        )

    with w4:
        st.metric(
            "💧 Humidity",
            f"{weather['humidity']}%"
        )

    st.info(
        f"Current Condition: {weather['condition']}"
    )

    st.divider()

    # ==========================
    # Airline History
    # ==========================

    st.subheader("📊 Airline History")

    history = result["history"]

    h1, h2, h3, h4 = st.columns(4)

    with h1:
        st.metric(
            "Cancellation Rate",
            f"{history['cancel_rate']}%"
        )

    with h2:
        st.metric(
            "Technical",
            history["technical"]
        )

    with h3:
        st.metric(
            "Operational",
            history["operational"]
        )

    with h4:
        st.metric(
            "Weather",
            history["weather"]
        )

    chart_data = pd.DataFrame(
        {
            "Count": [
                history["technical"],
                history["operational"],
                history["weather"]
            ]
        },
        index=[
            "Technical",
            "Operational",
            "Weather"
        ]
    )

    st.bar_chart(chart_data)

    st.divider()

    # ==========================
    # Delay Performance
    # ==========================

    st.subheader("⏱ Delay Performance")

    delay = result["delay"]

    d1, d2 = st.columns(2)

    with d1:
        st.metric(
            "On-Time Performance",
            f"{delay['on_time']}%"
        )

    with d2:
        st.metric(
            "Delayed Flights",
            delay["delayed_flights"]
        )

    st.divider()

    # ==========================
    # AI Analysis
    # ==========================

    st.subheader("🤖 AI Analysis")

    with st.chat_message("assistant"):
        st.write(
            result["explanation"]
        )