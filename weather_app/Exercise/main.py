import streamlit as st
import plotly.express as px
import pandas as pd

# title widget
st.title("In Search for Happiness")

# Add two selectboxes
option_x = st.selectbox('select the data for the X-axis',
                        ('GDP', 'Happiness', 'Generosity'))
option_y = st.selectbox('select the data for the Y-axis',
                        ('GDP', 'Happiness', 'Generosity'))


# Load the dataframe
df = pd.read_csv('happy.csv')


def get_data(option_x, option_y):
    if option_x == "Happiness":
        x_array = df["happiness"]
    elif option_x == "GDP":
        x_array = df["gdp"]
    else:
        x_array = df["generosity"]

    if option_y == "Happiness":
        y_array = df["happiness"]
    elif option_y == "GDP":
        y_array = df["gdp"]
    else:
        y_array = df["generosity"]
    return (x_array, y_array)


x_array, y_array = get_data(option_x, option_y)
# Add a subheader above thee plot to the webpage
st.subheader(f"{option_x} and {option_y}")

# create and add the plot to the webpage
figure1 = px.scatter(x=x_array, y=y_array, labels={
                     'x': option_x, 'y': option_y})
st.plotly_chart(figure1)
