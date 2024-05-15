import streamlit as st
import pandas as pd
import pickle

teams = ['Royal Challengers Bangalore',
 'Punjab Kings',
 'Delhi Capitals',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Lucknow Super Giants',
 'Gujarat Titans']

venue = ['M Chinnaswamy Stadium', 'Sheikh Zayed Stadium',
       'Dubai International Cricket Stadium', 'Wankhede Stadium',
       'M.Chinnaswamy Stadium',
       'Maharashtra Cricket Association Stadium, Pune',
       'Punjab Cricket Association IS Bindra Stadium',
       'Rajiv Gandhi International Stadium, Uppal',
       'Punjab Cricket Association Stadium, Mohali',
       'Arun Jaitley Stadium', 'Wankhede Stadium, Mumbai',
       'Feroz Shah Kotla', 'Sawai Mansingh Stadium',
       'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
       'Kingsmead', 'Eden Gardens', 'Sawai Mansingh Stadium, Jaipur',
       'Brabourne Stadium, Mumbai', 'Sharjah Cricket Stadium',
       'Eden Gardens, Kolkata', 'Buffalo Park',
       'Himachal Pradesh Cricket Association Stadium',
       'Narendra Modi Stadium, Ahmedabad',
       'Maharashtra Cricket Association Stadium',
       'Rajiv Gandhi International Stadium',
       'Sardar Patel Stadium, Motera', 'M Chinnaswamy Stadium, Bengaluru',
       'Dr DY Patil Sports Academy, Mumbai',
       'MA Chidambaram Stadium, Chepauk', 'Barabati Stadium',
       'Brabourne Stadium',
       'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'JSCA International Stadium Complex',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Zayed Cricket Stadium, Abu Dhabi', 'Holkar Cricket Stadium',
       'New Wanderers Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'OUTsurance Oval', 'SuperSport Park', "St George's Park",
       'Barsapara Cricket Stadium, Guwahati',
       'Vidarbha Cricket Association Stadium, Jamtha', 'Newlands',
       'MA Chidambaram Stadium', 'Arun Jaitley Stadium, Delhi',
       'MA Chidambaram Stadium, Chepauk, Chennai',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Dr DY Patil Sports Academy', 'De Beers Diamond Oval',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Probability Predictor')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

sel_veneu = st.selectbox('Select a venue', sorted(venue))
total_runs = st.number_input('Runs in 1st innings', min_value=0, step=1)

col3, col4, col5 = st.columns(3)
with col3:
    current_runs = st.number_input('Current runs', min_value=1, step=1)
with col4:
    overs = st.number_input('Overs', min_value=1, max_value=20, step=1)
with col5:
    wickets = st.number_input('Wickets', min_value=0, max_value=10, step=1)

if st.button('Predict Probability'):
    runs_left = total_runs - current_runs
    balls_left = 120 - overs*6
    wickets_left = 10 - wickets
    crr = current_runs/overs
    rrr = (runs_left*6)/balls_left

    data = pd.DataFrame({'venue': sel_veneu, 'batting_team': [batting_team], 'bowling_team': [bowling_team],
                        'total_runs_first_inning': [total_runs], 'runs_left': [runs_left], 'balls_left': [balls_left],
                            'wickets_left': [wickets_left], 'crr': [crr], 'rrr': [rrr]})

    pred = pipe.predict_proba(data)
    st.header('Winning Probability')
    st.header(f'{batting_team} : {round(pred[0][1]*100)} %')
    st.header(f'{bowling_team} : {round(pred[0][0]*100)} %')