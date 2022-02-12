import streamlit as st
import datetime as dt
import requests
import pytz

st.markdown('''# TaxiFareModel front''')



pickup_date = st.date_input('pickup date', value=dt.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup time', value=dt.datetime(2012, 10, 6, 12, 10, 20))


pickup_longitude = st.number_input('pickup longitude',format='%g')
pickup_latitude = st.number_input('pickup latitude', format='%g')
dropoff_longitude = st.number_input('dropoff longitude', format='%g')
dropoff_latitude = st.number_input('dropoff latitude', format='%g')
passenger_count = options = st.selectbox('passenger_count', (1, 2, 3, 4, 5, 6, 7, 8))

params = {
    "pickup_datetime": f'{pickup_date} {pickup_time}',
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_count)
}

url = 'https://taxifare.lewagon.ai/predict'

if params:

    if url == 'https://taxifare.lewagon.ai/predict':

        response = requests.get(url,params=params)

        prediction = response.json()
        #if type(prediction) == float:
        st.write(f'Price prediction: {round(prediction["fare"],2)} $')
