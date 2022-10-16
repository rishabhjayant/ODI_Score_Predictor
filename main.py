import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))

teams=['India', 'Australia', 'England', 'New Zealand', 'Sri Lanka',
       'West Indies', 'South Africa', 'Pakistan', 'Bangladesh', 'Afghanistan']


city=['other', 'London', 'Abu Dhabi', 'Manchester', 'Colombo', 'Birmingham',
       'Cardiff', 'Dubai', 'Nottingham', 'Sydney', 'Leeds', 'Southampton',
       'Guyana', 'Hamilton', 'Mount Maunganui', 'Wellington', 'Cape Town',
       'Johannesburg', 'Rangiri', 'Centurion', 'Pallekele', 'Port Elizabeth',
       'Sharjah', 'Melbourne', 'Mirpur', 'Christchurch', 'Durban', 'Auckland',
       'Dublin', 'Antigua', 'Barbados', 'St Kitts', 'Adelaide',
       'Chester-le-Street', 'Dhaka', 'Perth', 'Nelson', 'Visakhapatnam',
       'Bristol', 'Canberra', 'Chandigarh', 'Pune', 'Brisbane', 'Lucknow',
       'Harare', 'Dunedin', 'Mumbai', 'Taunton']


st.title('ODI Score Predictor')


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(city))

col3,col4, = st.columns(2)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works better for oversdone more than 20)')

col5,col6=st.columns(2)
with col5:
    first_batting = st.selectbox('select first batting or chasing',['First Batting','Chasing'])
with col6:
    wickets = st.number_input('Wickets out')

last_ten = st.number_input('Runs scored in last 10 overs')


if st.button('Predict Score'):
    balls_left = 300- (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs
    first=[]
    if first_batting=='First Batting':
           first=1
    else:
           first=0
    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_runs': [current_score],'deliveries_left': [balls_left], 'wicket_left': [wickets], 'current_run_rate': [crr], 'last_10_Over_runs': [last_ten],'first_batting':first})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))

