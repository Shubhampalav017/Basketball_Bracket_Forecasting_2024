
import streamlit as st
import pandas as pd

# Load data
@st.cache_data 
def load_data():
    return pd.read_csv('D:\Source\Orion_innovation_internship_repos\Basketball_Bracket_Forecasting_2024\myapp\Data\df_historic_tourney_features.csv')

df = load_data()

# Title and introduction
st.title('March Madness 2024 Analysis')
st.write('This app provides an analysis of historical tournament data for March Madness.')

# Display dataset overview
st.header('Dataset Overview')
st.write('### Sample Data')
st.dataframe(df.head())

st.write('### Dataset Statistics')
st.write(df.describe())

# Filter options
st.header('Filter Options')
seasons = df['Season'].unique()
selected_season = st.selectbox('Select Season', seasons)

filtered_df = df[df['Season'] == selected_season]

teams = filtered_df['TeamID'].unique()
selected_team = st.selectbox('Select Team', teams)

filtered_df = filtered_df[filtered_df['TeamID'] == selected_team]

st.write('### Filtered Data')
st.dataframe(filtered_df)

# Visualizations
st.header('Visualizations')
st.write('### Win Percentage Over Time')
win_pct_chart = filtered_df.groupby('Season')['WinPercentage'].mean().reset_index()
st.bar_chart(win_pct_chart.set_index('Season'))

st.write('### Score Differences')
score_diff_chart = filtered_df[['TeamScore', 'OppScore']]
st.bar_chart(score_diff_chart)


# Predictions
st.header('Game Predictions')
st.write('### Predict Game Outcome')
team_win_pct = st.number_input('Enter Team Win Percentage')
opp_win_pct = st.number_input('Enter Opponent Win Percentage')
chalk_seed_diff = st.number_input('Enter Chalk Seed Difference')

if st.button('Predict'):
    # Simple prediction logic based on the features
    if team_win_pct > opp_win_pct:
        st.write('Prediction: Team is likely to win')
    else:
        st.write('Prediction: Team is likely to lose')

st.write('### Baseline Prediction Results')
st.write('Number of correct baseline predictions:', df['BaselinePred'].sum())


# Title of the app
st.title("GitHub")

# Define the link you want to open
link = "https://github.com/Shubhampalav017/Basketball_Bracket_Forecasting_2024"

# Create a button and open the link when the button is clicked
if st.button("Open Link"):
    st.markdown(f'<a href="{link}" target="_blank">Click here to open the link</a>', unsafe_allow_html=True)

