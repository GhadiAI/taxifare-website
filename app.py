import streamlit as st
import requests


st.title("Taxi Fare Prediction")
st.write("Enter the details of your taxi ride to get a fare prediction:")


date_and_time = st.text_input("Date and Time (YYYY-MM-DD HH:MM:SS)")
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.slider("Number of Passengers", min_value=1, max_value=6, value=1)


if st.button("Predict Fare"):

    url = 'https://taxifare.lewagon.ai/predict'
    params = {
        "pickup_datetime": date_and_time,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        fare = response.json().get("fare")
        st.write(f"The predicted fare is ${fare:.2f}")
    else:
        st.write("There was an error with the prediction request.")