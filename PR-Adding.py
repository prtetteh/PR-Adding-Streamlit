import streamlit as st

# Set up the title with color
st.markdown("<h1 style='color:tomato; font-size: 40px;'>Fun Adding App for Toddlers</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:seagreen; font-size: 24px;'>Let's add two numbers together!</p>", unsafe_allow_html=True)

# Ask for the first number
first_number = st.number_input("Enter the first number:", min_value=0, step=1, key="num1", format="%d")

# Ask for the second number
second_number = st.number_input("Enter the second number:", min_value=0, step=1, key="num2", format="%d")

# Calculate the sum
result = first_number + second_number

# Display the result in a colorful format
st.markdown(f"<p style='color:royalblue; font-size: 24px;'>The sum is: {result}</p>", unsafe_allow_html=True)
