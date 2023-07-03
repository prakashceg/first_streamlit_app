import streamlit
streamlit.title("My Parents New Healthy Diner")

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:

streamlit.dataframe(my_fruit_list)
